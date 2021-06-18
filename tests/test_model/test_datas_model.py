import pytest
from app.models.datas_model import *
from . import *

def test_update(drop_all, datas):
    assert Datas.objects.count() == 0
    datas.save()
    assert Datas.objects.count() == 1
    data = {'values':'{value}'}
    datas.update(data)
    assert datas.values == data['values']
