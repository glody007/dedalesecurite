from flask import request
from flask_restplus import Resource, fields
from .utils import abort_404
from . import api_rest
from .resource_type import ResourceType
from ..services import TemplateService
from ..services import UserService
from ..services import DatasService
from .template import template_fields
from .validation import *
from .security import require_auth

datas_fields = api_rest.model('Datas', {
    'id': fields.String(attribute=lambda x: str(x.id)),
    'values': fields.String(required=True, min_length=1),
    'template_id': fields.String()
})

verification_fields = api_rest.model('Verification', {
    'can_view': fields.Boolean(),
    'datas': fields.Nested(datas_fields),
    'template': fields.Nested(template_fields)
})

datas_list_fields = api_rest.model('DatasList', {
    'list datas': fields.List(fields.Nested(datas_fields))
})

response_post_datas_fields = api_rest.model('Response post datas success', {
    'result': fields.String(required=True),
    'datas': fields.Nested(datas_fields)
})

@api_rest.route('/templates/<template_id>/list-datas')
class DatasList(Resource):
    @api_rest.marshal_with(datas_list_fields)
    @api_rest.response(200, 'Success', datas_list_fields)
    def get(self, template_id):
        return {'list datas' : DatasService.get_list(template_id)}, 200

    @api_rest.marshal_with(response_post_datas_fields)
    @api_rest.doc(security='apiKey')
    @require_auth()
    @api_rest.response(401, 'Unauthorized')
    @api_rest.expect(datas_fields, validate=True)
    @api_rest.response(201, 'Success')
    @api_rest.response(400, 'Validation Error')
    def post(self, template_id):
        user_id = UserService.get_id(request.headers.get('X-API-KEY'))
        datas = TemplateService.add_datas(request.json, template_id)
        return {'result': 'success', 'datas': datas}, 201

@api_rest.route('/datas/<datas_id>/verification')
class Verification(Resource):
    @api_rest.doc(security='apiKey')
    @api_rest.marshal_with(verification_fields)
    @api_rest.response(200, 'Success', datas_fields)
    @api_rest.response(404, 'Ressource not found')
    @validate_ObjectId_or_404('datas_id')
    def get(self, datas_id):
        datas = DatasService.get_or(datas_id, abort_404)
        template = TemplateService.get(datas.template_id)
        user_id = UserService.get_id(request.headers.get('X-API-KEY'))
        return {'can_view': user_id==template.creator_id, 'datas': datas, 'template': template}, 200

@api_rest.route('/datas/<datas_id>')
class Datas(Resource):
    @api_rest.marshal_with(datas_fields)
    @api_rest.response(200, 'Success', datas_fields)
    @api_rest.response(404, 'Ressource not found')
    @validate_ObjectId_or_404('datas_id')
    def get(self, datas_id):
        datas = DatasService.get_or(datas_id, abort_404)
        return datas, 200

    @api_rest.doc(security='apiKey')
    @require_auth(res_type=ResourceType.DATAS, id_name='datas_id')
    @api_rest.response(401, 'Unauthorized')
    @api_rest.expect(datas_fields, validate=True)
    @api_rest.response(201, 'Success')
    @api_rest.response(400, 'Validation Error')
    @api_rest.response(404, 'Ressource not found')
    @validate_ObjectId_or_404('datas_id')
    def put(self, datas_id):
        DatasService.update_or(datas_id, request.json, abort_404)
        return {'result': 'success'}, 201

    @api_rest.doc(security='apiKey')
    @require_auth(res_type=ResourceType.DATAS, id_name='datas_id')
    @api_rest.response(401, 'Unauthorized')
    @api_rest.response(201, 'Success')
    @api_rest.response(404, 'Ressource not found')
    @validate_ObjectId_or_404('datas_id')
    def delete(self, datas_id):
        DatasService.delete_or(datas_id, abort_404)
        return {'result': 'success'}, 200
