import pytest
from mongoengine import *
from flask import current_app
from mongoengine.connection import disconnect
from app.models.user_model import User
from app.models.template_model import Template
from app.models.datas_model import Datas
from app.models import init_db
from app import app

with app.app_context():
    app.config['TESTING'] = True
    init_db()

@pytest.fixture
def drop_all():
    Template.drop_collection()
    User.drop_collection()
    Datas.drop_collection()

@pytest.fixture(scope="module")
def exemple_template_data():
    return {'nom': "certificat",
            'document_model': "{'nom':'name'}",
            'datas_model': "{'name':'string'}",
            'creator_id': "23441888888"}

@pytest.fixture(scope="module")
def exemple_user_data():
    return {'nom': 'root',
            'password': 'password',
            'phone_number': "+2439999999",
            'email': "jjenda@jjenda.com"}

@pytest.fixture(scope="module")
def exemple_datas_data():
    return {'values': "{'nom':'alchemist', 'birthday':'4-3-1900'}",
            'template_id': "22888399390003"}

def insert_user(exemple_user_data):
    user = User(nom = exemple_user_data["nom"],
                phone_number = exemple_user_data["phone_number"],
                email = exemple_user_data["email"])
    User.insert(user)
    return user

def insert_template(exemple_template_data):
    template = Template(nom=exemple_template_data['nom'],
                        document_model=exemple_template_data['document_model'],
                        datas_model=exemple_template_data['datas_model'],
                        creator_id=exemple_template_data['creator_id'])
    template.save()
    return template

def insert_datas(exemple_datas_data, template_id):
    datas = Datas(values=exemple_datas_data['values'],
                  template_id=str(template_id))
    datas.save()
    return datas

@pytest.fixture(scope="module")
def user(exemple_user_data):
    return User(nom = exemple_user_data["nom"],
                phone_number = exemple_user_data["phone_number"],
                email = exemple_user_data["email"])

@pytest.fixture(scope="module")
def template(exemple_template_data):
    return Template(nom=exemple_template_data['nom'],
                    document_model=exemple_template_data['document_model'],
                    datas_model=exemple_template_data['datas_model'],
                    creator_id=exemple_template_data['creator_id'])

@pytest.fixture(scope="module")
def datas(exemple_datas_data):
    return Datas(values = exemple_datas_data["values"],
                 template_id = exemple_datas_data["template_id"])

def user_count():
    return User.objects.count()

def template_count():
    return Template.objects.count()

def datas_count():
    return Datas.objects.count()
