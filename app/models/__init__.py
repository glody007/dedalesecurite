from mongoengine import *
import os
from .plan_model import *
from .template_model import *
from .user_model import *
from .datas_model import *

def init_db():
    from flask import current_app

    if current_app.config['TESTING']:
        connect(host=current_app.config['DB_TEST_URI'])
    else:
        connect(host=current_app.config['DB_URI'])
        User.register_admin({'nom': current_app.config['ADMIN_NAME'],
                             'phone_number': current_app.config['ADMIN_NUMBER'],
                             'email': current_app.config['ADMIN_EMAIL'],
                             'password': current_app.config['ADMIN_PASSWORD']})
