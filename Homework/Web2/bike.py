from mongoengine import Document,StringField, IntField

class Bike(Document):
    model = StringField()
    fee = IntField()
    link = StringField()
    year = IntField()