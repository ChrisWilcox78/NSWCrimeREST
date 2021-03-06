# NSWCrimeREST
A RESTful API written in Python (using Flask, Flask-Sockets, and MongoEngine) and backed by either MongoDB or MySQL that exposes the NSW crime dataset (https://search.data.gov.au/dataset/ds-dga-6cdf7a25-4f2d-4bae-b3b5-61175e2b3b13/details).  The server also provides a websocket via which clients can register to receive updates as soon as they are saved to to the database.

The API is hosted with the smaller test dataset here <https://chriswilcox.pythonanywhere.com/> (websockets and importing are not enabled).  

Interactive OpenAPI documentation of the API is available in ReDoc format here <https://chriswilcox78.github.io/NSWCrimeREST-ApiDoc/> and in SwaggerUI format here <https://chriswilcox78.github.io/NSWCrimeREST-ApiDoc/swagger-ui/>.

## Some notes on the design
- I have taken a layered approach to the application separating it into persistence, business, and REST layers.  This will allow changes to be made to one of these layers without having to make corresponding changes to others (for example, adding an additional version of the persistence layer to use the relational MYSQL DBMS only required changes to that layer and a small change to the way the repository was referenced in the business layer - the new repository implementation satisfied the same duck-type as the mongo version).
- I have made of some [reactive programming constructs](http://reactivex.io/) in the code that drives the websocket implementation.  In particular, a Subject is used to monitor the repository for new crime reports and then push these new reports out to websocket clients who have registered an interest.  The websocket endpoint for subscription is at `/crime-report-updates`.
- Decorators are used to abstract away the details of cross-cutting concerns like validation or "boilerplate" concerns like connecting to the database and running some functionality in a background thread.
- The REST API provides basic resources for CrimeReports, CrimeLocations, and Offences.  It also provide links to satisfy the "Hypertext As The Engine Of Application State" constraint of a fully RESTful architecture.  A client needn't know anything about the API before hitting the root endpoint - it should be able to discover the functionality of the API through the links provided.
- A basic, operation-based REST resource for importing from a file has been provided (it just takes a string pointing the path of the file to load from).  This is meant as a basic illustration of the way in which business operations can be encapsulated within resources, avoiding the potential for business control flow logic to leak out into clients (see [here](https://www.thoughtworks.com/insights/blog/rest-api-design-resource-modeling) for some detailed discussion of this issue).  The import endpoint is at `/import`.
- The code also makes use of the (relatively) new static typing features of Python.

## How to make it go

### Requirements
- MongoDB (the [basic docker container from DockerHub](https://hub.docker.com/_/mongo/) should work fine) or MYSQL 5 (again the [docker container](https://hub.docker.com/_/mysql/) should work fine).
- I developed it using Python 3.6.5 and the code uses type annotations introduced in 3.6 so I guess you'll need at least that version.
- The Python library dependencies are captured in the requirements.txt file.

### Environmental configuration
- There are 8 environment variables available:
  1. `CRIMES_DATA_DIR` - the directory to listen for changes on in order to pull in new data (defaults to the `data` directory in the repo)
  2. `CRIMES_REPO_TYPE` the type of repository to use.  Use `MONGO` for MongoDB and anything else to get MySQL (defaults to `MONGO`)
  3. `MONGO_HOST` - the hostname of the Mongo instance being used (defaults to `localhost`)
  4. `MONGO_PORT` - the port of the Mongo instance being used (defaults to the standard Mongo port: `27017`)
  5. `CRIMES_MYSQL_HOST` - the hostname of the MySQL instance being used (defaults to `localhost`)
  6. `CRIMES_MYSQL_PORT` - the port of the MySQL instance being used (defaults to the standard MySQL port: `3306`)
  7. `CRIMES_MYSQL_USER` - the user used to connect to the MySQL instance being used (defaults to `crimes`)
  8. `CRIMES_MYSQL_USER_PW` - the password for `CRIMES_MYSQL_USER` (defaults to the VERY INSECURE `abc123`)
  
### Running
- There's a basic run configuration in `crimes.py` so can just run `python crimes.py`.
- Alternatively, you can use gunicorn - something like `gunicorn -k flask_sockets.worker crimes:app` should do the trick.  (Note: I've been having some issues with the file system listener permissions when running with gunicorn using the Windows Subsystem for Linux.  You can always use the ReST import endpoint if you run into similar difficulties.)

### A note on load times
- When I load the provided file using the standard MongoDB container with access to 4 processor cores and 4 GiB of RAM on a last generation (as of 5/2018) Dell XPS 15 with an i7  and 32 GiB of RAM, the load takes about 2 hours (obviously, YMMV).  Loads will likely take longer if you're using MySQL.  I have also provided a small test dataset; loading this should only take a minute or two.
