import pytest
from app.models.template_model import *
from . import *

def test_update(drop_all, template):
    assert Template.objects.count() == 0
    template.save()
    assert Template.objects.count() == 1
    assert template
    data = {'nom':'t',
            'document_model':'{doc}',
            'datas_model':'{datas}'}
    template.update(data)
    assert template.nom == data['nom']
    assert template.document_model == data['document_model']
    assert template.datas_model == data['datas_model']
