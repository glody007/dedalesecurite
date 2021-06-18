from . import *
from copy import deepcopy

def test_datas_list_get(drop_all, client, exemple_datas_data, exemple_template_data):
    template = insert_template(exemple_template_data)
    resp = client.get('/api/templates/{}/list-datas'.format(str(template.id)))
    assert len(resp.json['list datas']) == 0
    assert resp.status_code == 200
    insert_datas(exemple_datas_data, template.id)
    resp = client.get('/api/templates/{}/list-datas'.format(str(template.id)))
    assert len(resp.json['list datas']) == 1

def test_datas_list_post(drop_all, client, exemple_datas_data, exemple_template_data,exemple_user_data):
    resp = client.post('/api/auth/register', json=exemple_user_data)
    token_header = {'X-API-KEY': resp.json['auth_token']}

    resp_post = client.post('/api/templates', json=exemple_template_data, headers=token_header)
    template = resp_post.json['template']

    resp_post = client.post('/api/templates/{}/list-datas'.format(template['id']), json=exemple_datas_data, headers=token_header)
    assert resp_post.status_code == 201

    resp_get = client.get('/api/templates/{}/list-datas'.format(template['id']))
    assert len(resp_get.json['list datas']) == 1

    exemple = deepcopy(exemple_datas_data)
    exemple['values'] = ''
    resp_post = client.post('/api/templates/{}/list-datas'.format(template['id']), json=exemple)
    assert resp_post.status_code == 400

def test_datas_get(drop_all, client, exemple_datas_data, exemple_template_data):
    template = insert_template(exemple_template_data)
    datas = insert_datas(exemple_datas_data, template.id)
    resp_get = client.get('/api/datas/55153a8014829a865bbf700d')
    assert resp_get.status_code == 404
    resp_get = client.get('/api/datas/23')
    assert resp_get.status_code == 404
    resp_get = client.get('/api/datas/{}'.format(str(datas.id)))
    assert resp_get.status_code == 200
    assert resp_get.json['values'] == exemple_datas_data['values']

def test_datas_delete(drop_all, client, exemple_datas_data, exemple_template_data, exemple_user_data):
    resp = client.post('/api/auth/register', json=exemple_user_data)
    token_header = {'X-API-KEY': resp.json['auth_token']}

    resp_post = client.post('/api/templates', json=exemple_template_data, headers=token_header)
    template = resp_post.json['template']

    resp_post = client.post('/api/templates/{}/list-datas'.format(template['id']), json=exemple_datas_data, headers=token_header)
    assert resp_post.status_code == 201
    datas = resp_post.json['datas']

    resp_del = client.delete('/api/datas/55153a8014829a865bbf700d', headers=token_header)
    assert resp_del.status_code == 404
    resp_del = client.delete('/api/datas/23', headers=token_header)
    assert resp_del.status_code == 404
    assert datas_count() == 1
    resp_del = client.delete('/api/datas/{}'.format(datas['id']), headers=token_header)
    assert resp_del.status_code == 200
    assert datas_count() == 0

def test_datas_put(drop_all, client, exemple_datas_data, exemple_template_data, exemple_user_data):
    resp = client.post('/api/auth/register', json=exemple_user_data)
    token_header = {'X-API-KEY': resp.json['auth_token']}

    resp_put = client.put('/api/datas/55153a8014829a865bbf700d', json=exemple_datas_data, headers=token_header)
    assert resp_put.status_code == 404

    resp_put = client.put('/api/datas/23', json=exemple_datas_data, headers=token_header)
    assert resp_put.status_code == 404

    resp_post = client.post('/api/templates', json=exemple_template_data, headers=token_header)
    template = resp_post.json['template']

    resp_post = client.post('/api/templates/{}/list-datas'.format(template['id']), json=exemple_datas_data, headers=token_header)
    assert resp_post.status_code == 201
    datas = resp_post.json['datas']

    resp_put = client.put('/api/datas/{}'.format(datas['id']), json=exemple_datas_data, headers=token_header)
    assert resp_put.status_code == 201

    exemple = deepcopy(exemple_datas_data)
    exemple['values'] = ''
    resp_put = client.put('/api/datas/{}'.format(datas['id']), json=exemple, headers=token_header)
    assert resp_put.status_code == 400
