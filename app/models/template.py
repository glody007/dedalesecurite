from mongoengine import *
from .datas import *
import datetime

class Template(Document):
    name = StringField(required=True)
    document_model = StringField(required=True)
    datas_model = StringField(required=True)
    creator_id = StringField(required=True, default="")
    list_datas = ListField(ReferenceField(Datas))
