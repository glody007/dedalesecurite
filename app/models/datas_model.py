from mongoengine import *
import datetime

class Datas(Document):
    values = StringField(required=True)
    template_id = StringField(required=True, default="")

    def update(self, data):
        self.values = data['values']
        self.save()
