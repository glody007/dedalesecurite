from mongoengine import *
import os
from .plan_model import *
from .template_model import *
from .user_model import *
from .datas_model import *

def init_db():
    from flask import current_app

    connect(host=current_app.config['DB_URI'], alias='default')
    User.register_admin({'nom': current_app.config['ADMIN_NAME'],
                         'phone_number': current_app.config['ADMIN_NUMBER'],
                         'email': current_app.config['ADMIN_EMAIL'],
                         'password': current_app.config['ADMIN_PASSWORD']})
