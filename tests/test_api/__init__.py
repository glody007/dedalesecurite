import pytest
from app import app
from .. import (drop_all,
                insert_user,
                exemple_user_data,
                exemple_produit_data,
                user_count)

@pytest.fixture(scope="module")
def client():
    app.config['TESTING'] = True
    return app.test_client()
