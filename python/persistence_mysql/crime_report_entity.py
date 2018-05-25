from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .sqlalchemy_wiring import Base
from .offence_entity import OffenceEntity
from .location_entity import LocationEntity


class CrimeReportEntity(Base):
    __tablename__ = "crime_report"
    id = Column(Integer, primary_key=True)
    uuid = Column(String(60), nullable=False)
    time_period = Column(String(250), nullable=True)
    crime_count = Column(Integer, nullable=True)
    location_id = Column(Integer, ForeignKey("location.id"))
    location = relationship(LocationEntity, lazy="joined")
    offence_id = Column(Integer, ForeignKey("offence.id"))
    offence = relationship(OffenceEntity, lazy="joined")
