from flask import request, current_app
from flask_restplus import Resource, abort, fields
from . import api_rest
from ..models import  User as UserModel
from ..services import *
from .validation import *
from imagekitio import ImageKit

user_registration_info_fields  = api_rest.model('User registration info', {
    'nom': fields.String(required=True, min_length=3, max_length=50),
    'phone_number': fields.String(required=True, min_length=10, max_length=13),
    'email': fields.String(required=True),
    'password': fields.String(required=True, min_length=3),
    'longitude': fields.Float(),
    'latitude': fields.Float()
})

user_login_info_fields  = api_rest.model('User login info', {
    'password': fields.String(required=True, min_length=3, max_length=50),
    'email': fields.String(required=True)
})

imagekitio_resp_fields  = api_rest.model('ImageKitio response', {
    'token': fields.String(),
    'expire': fields.Integer(),
    'signature': fields.String()
})

@api_rest.route('/auth/register')
class Registration(Resource):
    @api_rest.expect(user_registration_info_fields, validate=True)
    @api_rest.response(201, 'Success')
    @api_rest.response(202, 'Fail. user with same email or phone number already exist')
    @api_rest.response(400, 'Validation Error')
    def post(self):
        try:
            auth_token = UserService.register(request.json)[1]
            return {'result': 'success', 'auth_token': auth_token.decode()}, 201
        except UserWithSameEmailError:
            return error_user_with_same_email
        except UserWithSameNumberError:
            return error_user_with_same_phone_number
        except:
            return error_email_and_phone_number


@api_rest.route('/auth/login')
class Login(Resource):
    @api_rest.expect(user_login_info_fields, validate=True)
    @api_rest.response(201, 'Success')
    @api_rest.response(400, 'Validation Error')
    @api_rest.response(401, 'Wrong credentials')
    def post(self):
        try:
            auth_token = UserService.login(request.json)
            return {'result': 'success', 'auth_token': auth_token.decode()}, 201
        except:
            return error_wrong_credentials


@api_rest.route('/auth/uploadendpoint')
class AuthImageUpload(Resource):
    @api_rest.response(200, 'Success', imagekitio_resp_fields)
    def get(self):
        imagekit = ImageKit(
            private_key=current_app.config['IMAGEKITIO_PRIVATE_KEY'],
            public_key=current_app.config['IMAGEKITIO_PUBLIC_KEY'],
            url_endpoint = current_app.config['IMAGEKITIO_URL_ENDPOINT']
        )

        auth_params = imagekit.get_authentication_parameters()
        return auth_params, 200
