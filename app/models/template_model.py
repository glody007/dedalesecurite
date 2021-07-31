from mongoengine import *
from .datas_model import *
import datetime

class Template(Document):
    nom = StringField(required=True)
    document_model = StringField(required=True)
    datas_model = StringField(required=True)
    creator_id = StringField(required=True, default="")
    list_datas = ListField(ReferenceField(Datas))
    blocked = BooleanField(default=False)
    protected = BooleanField(default=False)

    def update(self, data):
        self.nom = data['nom']
        self.document_model = data['document_model']
        self.datas_model = data['datas_model']
        self.save()

    def set_protected(self, data):
            self.protected = data['protected']
            self.save()
