"""
Global Flask Application Setting

See `.flaskenv` for default settings.
 """

import os
from app import app


class Config(object):
    # If not set fall back to production for safety
    FLASK_ENV =  os.getenv('FLASK_ENV', 'production')
    # Set FLASK_SECRET on your production Environment
    SECRET_KEY = os.getenv('FLASK_SECRET', 'Secret')
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')
    DB_URI = os.getenv('DB_URI')
    DB_TEST_URI = os.getenv('DB_TEST_URI')
    ADMIN_NAME = os.getenv('ADMIN_NAME')
    ADMIN_NUMBER = os.getenv('ADMIN_NUMBER')
    ADMIN_EMAIL = os.getenv('ADMIN_EMAIL')
    ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')
    IMAGEKITIO_PRIVATE_KEY = os.getenv('IMAGEKITIO_PRIVATE_KEY')
    IMAGEKITIO_PUBLIC_KEY = os.getenv('IMAGEKITIO_PUBLIC_KEY')
    IMAGEKITIO_URL_ENDPOINT = os.getenv('IMAGEKITIO_URL_ENDPOINT')

    APP_DIR = os.path.dirname(__file__)
    ROOT_DIR = os.path.dirname(APP_DIR)
    DIST_DIR = os.path.join(ROOT_DIR, 'dist')

    if not os.path.exists(DIST_DIR):
        raise Exception(
            'DIST_DIR not found: {}'.format(DIST_DIR))

app.config.from_object('app.config.Config')
