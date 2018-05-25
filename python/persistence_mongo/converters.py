from .location_doc import LocationMDoc
from .offence_doc import OffenceMDoc
from .crime_report_doc import CrimeReportMDoc
from business.crime_report import CrimeReport
from business.location import Location
from business.offence import Offence


def to_crime_report(doc: CrimeReportMDoc) -> CrimeReport:
    return CrimeReport(id=doc.id, time_period=doc.time_period, crime_count=doc.crime_count, location=to_location(doc.location), offence=to_offence(doc.offence))


def to_location(doc: LocationMDoc) -> Location:
    return Location(id=doc.id, statsArea=doc.statsArea, lga=doc.lga)


def to_offence(doc: OffenceMDoc) -> Offence:
    return Offence(id=doc.id, category=doc.category, subcategory=doc.subcategory)
