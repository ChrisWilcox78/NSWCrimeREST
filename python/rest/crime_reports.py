from flask import Blueprint, request

from business.retrieval_functions import (
    retrieveCrimeReport, searchCrimeReports)

from .decorators import json_content, treat_none_as_404

crimes_resource = Blueprint("crimes_resource", __name__)


@crimes_resource.route("/crime-reports/")
@json_content
def getCrimes():
    offenceId: str = request.args.get("offenceId", None)
    locationId: str = request.args.get("locationId", None)
    crimes: str = searchCrimeReports(
        offenceId=offenceId, locationId=locationId)
    return crimes


@crimes_resource.route('/crime-reports/<string:id>')
@json_content
@treat_none_as_404
def getCrime(id: str):
    return retrieveCrimeReport(id=id)
