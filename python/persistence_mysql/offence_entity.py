from sqlalchemy import Column, String, Integer
from .sqlalchemy_wiring import Base


class OffenceEntity(Base):
    __tablename__ = "offence"
    id = Column(Integer, primary_key=True)
    uuid = Column(String(60), nullable=False)
    category = Column(String(250), nullable=True)
    subcategory = Column(String(250), nullable=True)
