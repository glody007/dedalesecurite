import pytest
from mongoengine import *
from flask import current_app
from mongoengine.connection import disconnect
from app.models.user import User
from app.models import init_db
from app import app

with app.app_context():
    app.config['TESTING'] = True
    init_db()

@pytest.fixture
def drop_all():
    User.drop_collection()

@pytest.fixture(scope="module")
def exemple_produit_data():
    return {'prix': 10,
            'vendeur_id': "",
            'categorie': "phone",
            'description': "10GB",
            'url_photo': "akiri.com",
            'url_thumbnail_photo': "akiri.com",
            'longitude': 0,
            'latitude': 0}

@pytest.fixture(scope="module")
def exemple_user_data():
    return {'nom': 'root',
            'password': 'password',
            'phone_number': "+2439999999",
            'email': "jjenda@jjenda.com"}

def insert_user(exemple_user_data):
    user = User(nom = exemple_user_data["nom"],
                phone_number = exemple_user_data["phone_number"],
                email = exemple_user_data["email"])
    User.insert(user)
    return user

@pytest.fixture(scope="module")
def user(exemple_user_data):
    return User(nom = exemple_user_data["nom"],
                phone_number = exemple_user_data["phone_number"],
                email = exemple_user_data["email"])

def user_count():
    return User.objects.count()
