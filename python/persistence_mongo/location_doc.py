from mongoengine import Document, StringField


class LocationMDoc(Document):
    meta = {"collection": "location"}
    statsArea: str = StringField(required=True, unique_with="lga")
    lga: str = StringField(required=True)
