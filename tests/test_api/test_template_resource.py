from . import *
from copy import deepcopy

def test_template_list_get(drop_all, client, exemple_template_data):
    resp = client.get('/api/templates')
    assert len(resp.json['templates']) == 0
    assert resp.status_code == 200
    insert_template(exemple_template_data)
    resp = client.get('/api/templates')
    assert len(resp.json['templates']) == 1

def test_template_list_post(drop_all, client, exemple_template_data, exemple_user_data):
    resp_get = client.get('/api/templates')
    assert len(resp_get.json['templates']) == 0

    resp = client.post('/api/auth/register', json=exemple_user_data)
    token_header = {'X-API-KEY': resp.json['auth_token']}

    resp_post = client.post('/api/templates', json=exemple_template_data, headers=token_header)
    assert resp_post.status_code == 201

    resp_get = client.get('/api/templates')
    assert len(resp_get.json['templates']) == 1

    exemple = deepcopy(exemple_template_data)
    exemple['nom'] = ''
    resp_post = client.post('/api/templates', json=exemple)
    assert resp_post.status_code == 400

    exemple = deepcopy(exemple_template_data)
    exemple['document_model'] = ''
    resp_post = client.post('/api/templates', json=exemple)
    assert resp_post.status_code == 400

    exemple = deepcopy(exemple_template_data)
    exemple['datas_model'] = ''
    resp_post = client.post('/api/templates', json=exemple)
    assert resp_post.status_code == 400

def test_template_get(drop_all, client, exemple_template_data):
    template = insert_template(exemple_template_data)
    resp_get = client.get('/api/template/55153a8014829a865bbf700d')
    assert resp_get.status_code == 404
    resp_get = client.get('/api/template/23')
    assert resp_get.status_code == 404
    resp_get = client.get('/api/template/{}'.format(str(template.id)))
    assert resp_get.status_code == 200
    assert resp_get.json['nom'] == exemple_template_data['nom']

def test_template_delete(drop_all, client, exemple_template_data, exemple_user_data):
    resp = client.post('/api/auth/register', json=exemple_user_data)
    token_header = {'X-API-KEY': resp.json['auth_token']}

    resp_post = client.post('/api/templates', json=exemple_template_data, headers=token_header)
    assert resp_post.status_code == 201
    template = resp_post.json['template']

    resp_del = client.delete('/api/template/55153a8014829a865bbf700d', headers=token_header)
    assert resp_del.status_code == 404
    resp_del = client.delete('/api/template/23', headers=token_header)
    assert resp_del.status_code == 404
    assert template_count() == 1
    resp_del = client.delete('/api/template/{}'.format(template['id']), headers=token_header)
    assert resp_del.status_code == 200
    assert template_count() == 0

def test_template_put(drop_all, client, exemple_template_data, exemple_user_data):
    resp = client.post('/api/auth/register', json=exemple_user_data)
    token_header = {'X-API-KEY': resp.json['auth_token']}

    resp_put = client.put('/api/template/55153a8014829a865bbf700d', json=exemple_template_data, headers=token_header)
    assert resp_put.status_code == 404

    resp_put = client.put('/api/template/23', json=exemple_template_data, headers=token_header)
    assert resp_put.status_code == 404

    resp_post = client.post('/api/templates', json=exemple_template_data, headers=token_header)
    assert resp_post.status_code == 201
    template = resp_post.json['template']

    resp_put = client.put('/api/template/{}'.format(template['id']), json=exemple_template_data, headers=token_header)
    assert resp_put.status_code == 201

    exemple = deepcopy(exemple_template_data)
    exemple['nom'] = ''
    resp_put = client.put('/api/template/{}'.format(template['id']), json=exemple, headers=token_header)
    assert resp_put.status_code == 400

    exemple = deepcopy(exemple_template_data)
    exemple['document_model'] = ''
    resp_put = client.put('/api/template/{}'.format(template['id']), json=exemple)
    assert resp_put.status_code == 400
    exemple = deepcopy(exemple_template_data)
    exemple['datas_model'] = ''
    resp_put = client.put('/api/template/{}'.format(template['id']), json=exemple)
    assert resp_put.status_code == 400
