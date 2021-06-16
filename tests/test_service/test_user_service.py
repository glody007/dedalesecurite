import pytest
from app.services.user import UserService
from app.models.user import UserType
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

def test_register(drop_all, exemple_user_data):
    assert UserService.count() == 0
    user = UserService.register(exemple_user_data)
    assert UserService.count() == 1
    assert user.type == UserType.ENREGISTRER
    assert len(user.password_hash) > 10

def test_register_admin(drop_all, exemple_user_data):
    assert UserService.count() == 0
    user = UserService.register_admin(exemple_user_data)
    assert UserService.count() == 1
    assert user.type == UserType.ADMIN
    user = UserService.register_admin(exemple_user_data)
    assert UserService.count() == 1
