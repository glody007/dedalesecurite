""" Security Related things """
from functools import wraps
from flask import request
from flask_restplus import abort
from bson.objectid import ObjectId
from ..models import UserType
from ..services import DatasService, TemplateService, UserService
from .utils import abort_404
from .validation import error_invalid_auth_token
from .resource_type import ResourceType

authorizations = {
    'apiKey' : {
        'type' : 'apiKey',
        'in' : 'header',
        'name' : 'X-API-KEY'
    }
}

class AuthType:
    REGULAR = "regular"
    ADMIN = "admin"

def is_authorized(user_id, auth_type, res_type="", id_name=""):
    user = UserService.get(user_id)
    if user == None:
        return False
    # Admin give access
    elif user.type == UserType.ADMIN:
        return True
    # Require admin but not admin
    elif auth_type == AuthType.ADMIN:
        return False
    else:
        if res_type == "":
            return True
        # Test if id_name is in url
        id = request.view_args.get(id_name, None)
        if id == None:
            raise KeyError('{} doesnt match any route parameter'.format(id_name))
        if not ObjectId.is_valid(id):
            abort(404)
        if res_type == ResourceType.USER:
            return str(user.id) == id
        elif res_type == ResourceType.DATAS:
            datas = DatasService.get_or(id, abort_404)
            template = TemplateService.get_or(datas.template_id, abort_404)
            return str(user.id) == template.creator_id
        else:
            template = template = TemplateService.get_or(id, abort_404)
            return str(user.id) == template.creator_id

def require_auth(type=AuthType.REGULAR, res_type="", id_name=""):
    def actual_require_auth_decorator(func):
        """ Secure method decorator """
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Check if token in header
            auth_token = request.headers.get('X-API-KEY')
            if auth_token:
                # Check if token is valid
                resp = UserService.get_id(auth_token)
                if ObjectId.is_valid(resp):
                    if is_authorized(resp, type, res_type, id_name):
                        return func(*args, **kwargs)
                    else:
                        return abort(401)
                else:
                    return {
                              "result": "fail",
                              "message": resp
                           }, 401
            else:
                return error_invalid_auth_token
        return wrapper
    return actual_require_auth_decorator
