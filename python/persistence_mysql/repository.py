from typing import List, Optional
from uuid import uuid4

from business.crime_report import CrimeReport
from business.crime_report_observable import observe_crime_report
from business.location import Location
from business.offence import Offence

from .converters import to_crime_report, to_location, to_offence
from .location_entity import LocationEntity
from .offence_entity import OffenceEntity
from .crime_report_entity import CrimeReportEntity
from .sqlalchemy_wiring import get_session

MAX_RESULTS = 500


def retrieveAllCrimeReports() -> List[CrimeReport]:
    session = get_session()
    report_list = [to_crime_report(entity)
                   for entity in session.query(CrimeReportEntity).limit(MAX_RESULTS).all()]
    session.close()
    return report_list


def searchCrimeReports(offenceId: str, locationId: str) -> List[CrimeReport]:
    session = get_session()
    query = session.query(CrimeReportEntity)
    search_result = None
    if offenceId is None:
        search_result = [to_crime_report(entity) for entity in query.filter(
            LocationEntity.uuid == locationId).limit(MAX_RESULTS).all()]
    elif locationId is None:
        search_result = [to_crime_report(entity) for entity in query.filter(
            OffenceEntity.uuid == offenceId).limit(MAX_RESULTS).all()]
    else:
        search_result = [to_crime_report(entity) for entity in query.filter(OffenceEntity.uuid == offenceId).filter(
            LocationEntity.uuid == locationId).limit(MAX_RESULTS).all()]
    session.close()
    return search_result


def retrieveCrimeReport(id: str) -> Optional[CrimeReport]:
    session = get_session()
    report = to_crime_report(session.query(CrimeReportEntity).filter(
        CrimeReportEntity.uuid == id).one_or_none())
    session.close()
    return report


@observe_crime_report
def persist_crime_report(crime_report: CrimeReport) -> CrimeReport:
    session = get_session()
    location: LocationEntity = _persist_or_retrieve_location(
        crime_report.location, session)
    offence: OffenceEntity = _persist_or_retrieve_offence(
        crime_report.offence, session)
    crime_report_entity = CrimeReportEntity(uuid=str(uuid4()), time_period=crime_report.time_period,
                                            crime_count=crime_report.crime_count, location=location, offence=offence)
    session.add(crime_report_entity)
    session.commit()
    stored_report = to_crime_report(crime_report_entity)
    session.close()
    return stored_report


def retrieveLocation(id: str) -> Optional[Location]:
    session = get_session()
    location = to_location(session.query(
        LocationEntity).filter(LocationEntity.uuid == id).one_or_none())
    session.close()
    return location


def retrieveAllLocations() -> List[Location]:
    session = get_session()
    location_list = [to_location(entity)
                     for entity in session.query(LocationEntity).limit(MAX_RESULTS).all()]
    session.close()
    return location_list


def retrieveAllOffences() -> List[Offence]:
    session = get_session()
    offence_list = [to_offence(entity)
                    for entity in session.query(OffenceEntity).limit(MAX_RESULTS).all()]
    session.close()
    return offence_list


def retrieveOffence(id: str) -> Optional[Offence]:
    session = get_session()
    offence = to_offence(session.query(OffenceEntity).filter(
        OffenceEntity.uuid == id).one_or_none())
    session.close()
    return offence


def _persist_or_retrieve_location(location: Location, session) -> LocationEntity:
    location_entity = session.query(LocationEntity).filter(LocationEntity.lga == location.lga).filter(
        LocationEntity.statsArea == location.statsArea).one_or_none()
    if location_entity is None:
        location_entity = LocationEntity(
            uuid=str(uuid4()), lga=location.lga, statsArea=location.statsArea)
        session.add(location_entity)
    return location_entity


def _persist_or_retrieve_offence(offence: Offence, session) -> OffenceEntity:
    offence_entity = session.query(OffenceEntity).filter(OffenceEntity.category == offence.category).filter(
        OffenceEntity.subcategory == offence.subcategory).one_or_none()
    if offence_entity is None:
        offence_entity = OffenceEntity(
            uuid=str(uuid4()), category=offence.category, subcategory=offence.subcategory)
        session.add(offence_entity)
    return offence_entity
