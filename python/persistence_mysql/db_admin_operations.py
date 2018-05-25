from .location_entity import LocationEntity
from .offence_entity import OffenceEntity
from .crime_report_entity import CrimeReportEntity
from .sqlalchemy_wiring import Base, get_engine


def generateSchema():
    Base.metadata.create_all(get_engine())
