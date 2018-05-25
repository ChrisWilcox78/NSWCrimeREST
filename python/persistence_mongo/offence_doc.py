from mongoengine import Document, StringField


class OffenceMDoc(Document):
    meta = {"collection": "offence"}
    category: str = StringField(required=True, unique_with="subcategory")
    subcategory: str = StringField(required=False)
