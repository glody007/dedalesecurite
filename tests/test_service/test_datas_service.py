import pytest
from app.services.datas_service import *
from . import *
from .. import (drop_all,
                exemple_datas_data)

def test_create(exemple_datas_data):
    datas = DatasService.create(exemple_datas_data)
    assert datas.values == exemple_datas_data['values']
    assert datas.template_id == exemple_datas_data['template_id']

def test_insert(drop_all, exemple_datas_data):
    assert DatasService.count() == 0
    DatasService.insert(exemple_datas_data)
    assert DatasService.count() == 1

def test_delete_or(drop_all, exemple_datas_data):
    datas = DatasService.insert(exemple_datas_data)
    assert DatasService.count() == 1
    with pytest.raises(ValueError):
        DatasService.delete_or('55153a8014829a865bbf700d', raiseError)
    DatasService.delete_or(datas.id, raiseError)
    assert DatasService.count() == 0

def test_get_or(drop_all, exemple_datas_data):
    datas = DatasService.insert(exemple_datas_data)
    with pytest.raises(ValueError):
        DatasService.get_or('55153a8014829a865bbf700d', raiseError)
    DatasService.get_or(datas.id, raiseError)

def test_update_or(drop_all, exemple_datas_data):
    datas = DatasService.insert(exemple_datas_data)
    data = {'values':'{value}'}
    with pytest.raises(ValueError):
        DatasService.update_or('55153a8014829a865bbf700d', data, raiseError)

    DatasService.update_or(datas.id, data, raiseError)
    datas = DatasService.get(datas.id)
    assert datas.values == data['values']
