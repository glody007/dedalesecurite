from flask import request
from flask_restplus import Resource, fields
from .utils import abort_404
from . import api_rest
from .resource_type import ResourceType
from ..services import TemplateService
from ..services import UserService
from .validation import *
from .security import require_auth

template_fields = api_rest.model('Template', {
    'id': fields.String(attribute=lambda x: str(x.id)),
    'nom': fields.String(required=True, min_length=1),
    'document_model': fields.String(required=True, min_length=2),
    'datas_model': fields.String(required=True, min_length=2),
    'protected': fields.Boolean(),
    'creator_id': fields.String()
})

template_protect_fields = api_rest.model('TemplateProtect', {
    'blocked': fields.Boolean()
})

template_list_fields = api_rest.model('TemplateList', {
    'templates': fields.List(fields.Nested(template_fields))
})

response_post_template_fields = api_rest.model('Response post template success', {
    'result': fields.String(required=True),
    'template': fields.Nested(template_fields)
})

@api_rest.route('/templates')
class TemplateList(Resource):
    @api_rest.marshal_with(template_list_fields)
    @api_rest.doc(security='apiKey')
    @require_auth()
    @api_rest.response(200, 'Success', template_list_fields)
    def get(self):
        user_id = UserService.get_id(request.headers.get('X-API-KEY'))
        return {'templates' : TemplateService.get_list(user_id)}, 200

    @api_rest.marshal_with(response_post_template_fields)
    @api_rest.doc(security='apiKey')
    @require_auth()
    @api_rest.response(401, 'Unauthorized')
    @api_rest.expect(template_fields, validate=True)
    @api_rest.response(201, 'Success')
    @api_rest.response(400, 'Validation Error')
    def post(self):
        user_id = UserService.get_id(request.headers.get('X-API-KEY'))
        template = UserService.add_template(request.json, user_id)
        return {'result': 'success', 'template': template}, 201

@api_rest.route('/template/<template_id>/set-protected')
class TemplateProtection(Resource):
    @api_rest.doc(security='apiKey')
    @require_auth(res_type=ResourceType.TEMPLATE, id_name='template_id')
    @api_rest.response(401, 'Unauthorized')
    @api_rest.expect(template_protect_fields, validate=True)
    @api_rest.response(201, 'Success')
    @api_rest.response(404, 'Ressource not found')
    @validate_ObjectId_or_404('template_id')
    def post(self, template_id):
        TemplateService.set_protected_or(template_id, request.json, abort_404)
        return {'result': 'success'}, 201

@api_rest.route('/template/<template_id>')
class Template(Resource):
    @api_rest.marshal_with(template_fields)
    @api_rest.response(200, 'Success', template_fields)
    @api_rest.response(404, 'Ressource not found')
    @validate_ObjectId_or_404('template_id')
    def get(self, template_id):
        template = TemplateService.get_or(template_id, abort_404)
        return template, 200

    @api_rest.doc(security='apiKey')
    @require_auth(res_type=ResourceType.TEMPLATE, id_name='template_id')
    @api_rest.response(401, 'Unauthorized')
    @api_rest.expect(template_fields, validate=True)
    @api_rest.response(201, 'Success')
    @api_rest.response(400, 'Validation Error')
    @api_rest.response(404, 'Ressource not found')
    @validate_ObjectId_or_404('template_id')
    def put(self, template_id):
        TemplateService.update_or(template_id, request.json, abort_404)
        return {'result': 'success'}, 201

    @api_rest.doc(security='apiKey')
    @require_auth(res_type=ResourceType.TEMPLATE, id_name='template_id')
    @api_rest.response(401, 'Unauthorized')
    @api_rest.response(201, 'Success')
    @api_rest.response(404, 'Ressource not found')
    @validate_ObjectId_or_404('template_id')
    def delete(self, template_id):
        TemplateService.delete_or(template_id, abort_404)
        return {'result': 'success'}, 200
