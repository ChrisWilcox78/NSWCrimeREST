from flask import Blueprint
from business.retrieval_functions import retrieveAllOffences, retrieveOffence, searchCrimeReports
from .decorators import json_content

offences_resource = Blueprint("offences_resource", __name__)


@offences_resource.route("/offences/")
@json_content
def getOffences():
    return retrieveAllOffences()


@offences_resource.route("/offences/<string:id>")
@json_content
def getOffence(id: str):
    return retrieveOffence(id=id)


@offences_resource.route("/offences/<string:id>/crime-reports/")
@json_content
def getCrimesForOffence(id: str):
    return searchCrimeReports(offenceId=id)
