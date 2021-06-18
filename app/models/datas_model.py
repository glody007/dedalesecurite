from mongoengine import *
import datetime

class Datas(Document):
    values = StringField(required=True)
    template_id = StringField(required=True, default="")
