import pytest
from app import app
from .. import (drop_all,
                insert_user,
                insert_template,
                insert_datas,
                exemple_template_data,
                exemple_user_data,
                exemple_datas_data,
                user_count,
                template_count,
                datas_count)

@pytest.fixture(scope="module")
def client():
    app.config['TESTING'] = True
    return app.test_client()
