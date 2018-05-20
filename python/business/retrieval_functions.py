from mongoengine import connect
from business.location import Location
from business.offence import Offence
from business.crime_report import CrimeReport
from bson.objectid import ObjectId
import persistence.mongo_repository as repo
from business.validators import validate_before, provided
from typing import List


def searchCrimeReports(offenceId: str = None, locationId: str = None) -> List[CrimeReport]:
    """
    Search for crime reports using the specified criteria.  Specifying no criteria results in all records being returned.
    """
    if offenceId is None and locationId is None:
        return repo.retrieveAllCrimeReports()
    return repo.searchCrimeReports(offenceId=offenceId, locationId=locationId)


@validate_before(provided("id"))
def retrieveCrimeReport(id: str) -> CrimeReport:
    return repo.retrieveCrimeReport(id)


@validate_before(provided("id"))
def retrieveLocation(id: str) -> Location:
    return repo.retrieveLocation(id)


@validate_before(provided("id"))
def retrieveOffence(id: str) -> Offence:
    return repo.retrieveOffence(id)


def retrieveAllLocations() -> List[Location]:
    return repo.retrieveAllLocations()


def retrieveAllOffences() -> List[Offence]:
    return repo.retrieveAllOffences()
