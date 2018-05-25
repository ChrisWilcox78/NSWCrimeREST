from typing import Optional

from business.crime_report import CrimeReport
from business.location import Location
from business.offence import Offence
from .location_entity import LocationEntity
from .offence_entity import OffenceEntity
from .crime_report_entity import CrimeReportEntity


def to_crime_report(entity: Optional[CrimeReportEntity]) -> Optional[CrimeReport]:
    if entity is None:
        return None
    return CrimeReport(id=entity.uuid, time_period=entity.time_period, crime_count=entity.crime_count, location=to_location(entity.location), offence=to_offence(entity.offence))


def to_location(entity: Optional[LocationEntity]) -> Optional[Location]:
    if entity is None:
        return None
    return Location(id=entity.uuid, statsArea=entity.statsArea, lga=entity.lga)


def to_offence(entity: Optional[OffenceEntity]) -> Optional[Offence]:
    if entity is None:
        return None
    return Offence(id=entity.uuid, category=entity.category, subcategory=entity.subcategory)
