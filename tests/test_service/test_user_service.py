import pytest
from app.services.user_service import *
from app.models.user_model import UserType
from . import raiseError
from .. import (drop_all,
                exemple_user_data)

def test_create(exemple_user_data):
    user = UserService.create(exemple_user_data)
    assert user.nom == exemple_user_data['nom']
    assert user.email == exemple_user_data['email']
    assert user.type == UserType.ENREGISTRER
    assert user.phone_number ==  exemple_user_data['phone_number']

def test_add(drop_all, exemple_user_data):
    user = UserService.create(exemple_user_data)
    assert UserService.count() == 0
    UserService.add(user)
    assert UserService.count() == 1

def test_insert(drop_all, exemple_user_data):
    assert UserService.count() == 0
    UserService.insert(exemple_user_data)
    assert UserService.count() == 1

def test_delete_or(drop_all, exemple_user_data):
    user = UserService.insert(exemple_user_data)
    assert UserService.count() == 1
    with pytest.raises(ValueError):
        UserService.delete_or('55153a8014829a865bbf700d', raiseError)
    UserService.delete_or(user.id, raiseError)
    assert UserService.count() == 0

def test_get_or(drop_all, exemple_user_data):
    user = UserService.insert(exemple_user_data)
    with pytest.raises(ValueError):
        UserService.get_or('55153a8014829a865bbf700d', raiseError)
    UserService.get_or(user.id, raiseError)

def test_update_or(drop_all, exemple_user_data):
    user = UserService.insert(exemple_user_data)
    data = {'nom':'root', 'phone_number':'9999966666', 'email':'rot@root.com'}
    with pytest.raises(ValueError):
        UserService.update_or('55153a8014829a865bbf700d', data, raiseError)

    UserService.update_or(user.id, data, raiseError)
    user = UserService.get(user.id)
    assert user.nom == data['nom']
    assert user.email == data['email']
    assert user.type == UserType.ENREGISTRER
    assert user.phone_number ==  data['phone_number']

def test_register(drop_all, exemple_user_data):
    assert UserService.count() == 0
    user, auth_token = UserService.register(exemple_user_data)
    assert auth_token is not None
    assert UserService.count() == 1
    assert user.type == UserType.ENREGISTRER
    assert len(user.password_hash) > 10
    with pytest.raises(UserWithSameEmailError):
        UserService.register({'nom':'root', 'phone_number':'0997766555555', 'email':exemple_user_data['email']})
    with pytest.raises(UserWithSameNumberError):
        UserService.register({'nom':'root', 'phone_number':exemple_user_data['phone_number'], 'email':'hack@hack.com'})


def test_register_admin(drop_all, exemple_user_data):
    assert UserService.count() == 0
    user, auth_token = UserService.register_admin(exemple_user_data)
    assert UserService.count() == 1
    assert user.type == UserType.ADMIN
    with pytest.raises(UserWithSameEmailError):
        UserService.register_admin({'nom':'root', 'phone_number':'0997766555555', 'email':exemple_user_data['email']})
    with pytest.raises(UserWithSameNumberError):
        UserService.register_admin({'nom':'root', 'phone_number':exemple_user_data['phone_number'], 'email':'hack@hack.com'})
