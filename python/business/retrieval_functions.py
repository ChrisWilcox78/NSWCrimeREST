from typing import List

from business.location import Location
from business.offence import Offence

from .crime_report import CrimeReport
from .validators import provided, validate_before
from .repository_manager import get_configured_repo

repo = get_configured_repo()


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
