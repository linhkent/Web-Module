from mongoengine import Document,StringField, IntField

class Food(Document):
    title = StringField()
    link = StringField()