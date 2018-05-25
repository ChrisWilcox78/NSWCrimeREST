from sqlalchemy import Column, String, Integer
from .sqlalchemy_wiring import Base


class LocationEntity(Base):
    __tablename__ = "location"
    id = Column(Integer, primary_key=True)
    uuid = Column(String(60), nullable=False)
    statsArea = Column(String(250), nullable=True)
    lga = Column(String(250), nullable=True)
