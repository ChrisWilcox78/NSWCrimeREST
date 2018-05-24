from flask import Blueprint
from business.retrieval_functions import retrieveAllLocations, retrieveLocation, searchCrimeReports
from .decorators import json_content, treat_none_as_404

locations_resource = Blueprint("locations_resource", __name__)


@locations_resource.route("/crime-locations/")
@json_content
def getLocations():
    return retrieveAllLocations()


@locations_resource.route("/crime-locations/<string:id>")
@json_content
@treat_none_as_404
def getLocation(id: str):
    return retrieveLocation(id=id)


@locations_resource.route("/crime-locations/<string:id>/crime-reports/")
@json_content
def getCrimesForLocation(id: str):
    return searchCrimeReports(locationId=id)
