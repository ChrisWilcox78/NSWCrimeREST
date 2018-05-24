from json import dumps

from flask import Flask, jsonify, url_for
from flask_sockets import Sockets

from business.crime_report_observable import \
    OBSERVABLE_INSTANCE as REPORTS_OBSERVABLE
from rest.crime_reports import crimes_resource
from rest.decorators import run_in_thread
from rest.import_resource import import_resource
from rest.json_serializer import to_serializable
from rest.locations import locations_resource
from rest.offences import offences_resource

from werkzeug.exceptions import BadRequest

app = Flask(__name__)
app.register_blueprint(locations_resource)
app.register_blueprint(offences_resource)
app.register_blueprint(crimes_resource)
app.register_blueprint(import_resource)


@app.route("/")
def root():
    return jsonify([
        {
            "resource": "crime_reports",
            "url": url_for("crimes_resource.getCrimes", _external=True)
        }, {
            "resource": "crime_locations",
            "url": url_for("locations_resource.getLocations", _external=True)
        }, {
            "resource": "offences",
            "url": url_for("offences_resource.getOffences", _external=True)
        }
    ])


@app.errorhandler(ValueError)
def handle_value_error(error):
    raise BadRequest()


sockets = Sockets(app)


@sockets.route("/crime-report-updates")
def subscribe_to_crime_reports(ws):
    handle_crime_socket_sub(ws)


def handle_crime_socket_sub(ws):
    subscription = REPORTS_OBSERVABLE.subscribe(get_report_sender(ws))
    while not ws.closed:
        # need to receive to detect client closure
        ws.receive()
    subscription.dispose()


def get_report_sender(ws):
    def send_report(report):
        # need to push context here so that url strings can be generated
        with app.test_request_context():
            if not ws.closed:
                ws.send(dumps(to_serializable(report)))
    return send_report


# TESTING FROM HERE
if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
