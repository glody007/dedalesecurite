import pytest
from app.services.template_service import *
from . import *
from .. import (drop_all,
                exemple_template_data)

def test_create(exemple_template_data):
    template = TemplateService.create(exemple_template_data)
    assert template.nom == exemple_template_data['nom']
    assert template.document_model == exemple_template_data['document_model']
    assert template.datas_model == exemple_template_data['datas_model']
    assert template.creator_id == exemple_template_data['creator_id']

def test_insert(drop_all, exemple_template_data):
    assert TemplateService.count() == 0
    TemplateService.insert(exemple_template_data)
    assert TemplateService.count() == 1

def test_delete_or(drop_all, exemple_template_data):
    template = TemplateService.insert(exemple_template_data)
    assert TemplateService.count() == 1
    with pytest.raises(ValueError):
        TemplateService.delete_or('55153a8014829a865bbf700d', raiseError)
    TemplateService.delete_or(template.id, raiseError)
    assert TemplateService.count() == 0

def test_get_or(drop_all, exemple_template_data):
    template = TemplateService.insert(exemple_template_data)
    with pytest.raises(ValueError):
        TemplateService.get_or('55153a8014829a865bbf700d', raiseError)
    TemplateService.get_or(template.id, raiseError)

def test_update_or(drop_all, exemple_template_data):
    template = TemplateService.insert(exemple_template_data)
    data = {'nom':'t', 'document_model':'{doc}', 'datas_model':'{datas}'}
    with pytest.raises(ValueError):
        TemplateService.update_or('55153a8014829a865bbf700d', data, raiseError)

    TemplateService.update_or(template.id, data, raiseError)
    template = TemplateService.get(template.id)
    assert template.nom == data['nom']
    assert template.document_model == data['document_model']
    assert template.datas_model == data['datas_model']
