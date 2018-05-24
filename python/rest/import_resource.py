from flask import Blueprint, request
from threading import Thread
from business.csv_processor import process_csv
from .decorators import run_in_thread
from werkzeug.exceptions import BadRequest

import_resource = Blueprint("import_resource", __name__)


@import_resource.route("/import/", methods=["POST"])
def import_crimes():
    if request.headers["Content-Type"] == "application/json":
        filename = request.get_json()["filename"]
        if filename is None:
            raise BadRequest("filename must be provided")
        _importFromCsv(filename)
        return "Import started", 201


@run_in_thread
def _importFromCsv(filename):
    process_csv(filename)
