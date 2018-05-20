from persistence.decorators import db_connect
from persistence.location_doc import LocationMDoc
from persistence.offence_doc import OffenceMDoc
from persistence.crime_report_doc import CrimeReportMDoc
from business.crime_report import CrimeReport
from business.location import Location
from business.offence import Offence
from bson.objectid import ObjectId
from persistence.converters import to_crime_report, to_location, to_offence
from typing import List

MAX_RESULTS = 500


@db_connect
def retrieveAllCrimeReports() -> List[CrimeReport]:
    return [to_crime_report(doc) for doc in CrimeReportMDoc.objects.limit(MAX_RESULTS)]  # pylint: disable=no-member


@db_connect
def searchCrimeReports(offenceId: str, locationId: str) -> List[CrimeReport]:
    if offenceId is None:
        reports = CrimeReportMDoc.objects(location=ObjectId(   # pylint: disable=no-member
            locationId)).limit(MAX_RESULTS)
    elif locationId is None:
        reports = CrimeReportMDoc.objects(offence=ObjectId(   # pylint: disable=no-member
            offenceId)).limit(MAX_RESULTS)
    else:
        reports = CrimeReportMDoc.objects(offence=ObjectId(offenceId), location=ObjectId(   # pylint: disable=no-member
            locationId)).limit(MAX_RESULTS)
    return [to_crime_report(doc) for doc in reports]


@db_connect
def retrieveCrimeReport(id: str) -> CrimeReport:
    return to_crime_report(CrimeReportMDoc.objects.get(id=ObjectId(id)))  # pylint: disable=no-member


@db_connect
def persist_crime_report(crime_report: CrimeReport) -> None:
    offence_doc: OffenceMDoc = _persist_or_retrieve_offence(
        crime_report.offence)
    location_doc: LocationMDoc = _persist_or_retrieve_location(
        crime_report.location)
    crime_report_doc: CrimeReportMDoc = CrimeReportMDoc(
        time_period=crime_report.time_period, crime_count=crime_report.crime_count, location=location_doc, offence=offence_doc)
    crime_report_doc.save()


@db_connect
def retrieveLocation(id: str) -> Location:
    return to_location(LocationMDoc.objects.get(id=ObjectId(id)))  # pylint: disable=no-member


@db_connect
def retrieveAllLocations() -> List[Location]:
    return [to_location(doc) for doc in LocationMDoc.objects]  # pylint: disable=no-member


@db_connect
def retrieveAllOffences() -> List[Offence]:
    return [to_offence(doc) for doc in OffenceMDoc.objects]  # pylint: disable=no-member


@db_connect
def retrieveOffence(id: str) -> Offence:
    return to_offence(OffenceMDoc.objects.get(id=ObjectId(id)))  # pylint: disable=no-member


def _persist_or_retrieve_location(location: Location) -> LocationMDoc:
    location_doc = LocationMDoc.objects(  # pylint: disable=no-member
        statsArea=location.statsArea, lga=location.lga).first()
    if location_doc is None:
        location_doc = LocationMDoc(
            statsArea=location.statsArea, lga=location.lga)
        location_doc.save()
    return location_doc


def _persist_or_retrieve_offence(offence: Offence) -> OffenceMDoc:
    offence_doc = OffenceMDoc.objects(  # pylint: disable=no-member
        category=offence.category, subcategory=offence.subcategory).first()
    if offence_doc is None:
        offence_doc = OffenceMDoc(
            category=offence.category, subcategory=offence.subcategory)
        offence_doc.save()
    return offence_doc
