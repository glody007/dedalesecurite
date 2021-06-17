import pytest
from app import app
from .. import (drop_all,
                insert_user,
                insert_template,
                exemple_template_data,
                exemple_user_data,
                user_count,
                template_count)

@pytest.fixture(scope="module")
def client():
    app.config['TESTING'] = True
    return app.test_client()
