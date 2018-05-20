from persistence.location_doc import LocationMDoc
from persistence.offence_doc import OffenceMDoc
from mongoengine import Document, StringField, IntField, ReferenceField


class CrimeReportMDoc(Document):
    meta = {"collection": "crime_report"}
    time_period: str = StringField(required=True)
    crime_count: int = IntField(required=True)
    location: LocationMDoc = ReferenceField(
        document_type=LocationMDoc, required=True)
    offence: OffenceMDoc = ReferenceField(
        document_type=OffenceMDoc, required=True)
