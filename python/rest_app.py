from flask import Flask, url_for, jsonify
from rest.locations import locations_resource
from rest.offences import offences_resource
from rest.crime_reports import crimes_resource
from rest.import_resource import import_resource

app = Flask(__name__)
app.register_blueprint(locations_resource)
app.register_blueprint(offences_resource)
app.register_blueprint(crimes_resource)
app.register_blueprint(import_resource)


@app.route("/")
def root():
    return jsonify({
        "crime_reports": url_for("crimes_resource.getCrimes", _external=True),
        "crime_locations": url_for("locations_resource.getLocations", _external=True),
        "offences": url_for("offences_resource.getOffences", _external=True)
    })


# TESTING FROM HERE

def _runServer():
    app.run(debug=True, threaded=True)


if __name__ == "__main__":
    _runServer()
