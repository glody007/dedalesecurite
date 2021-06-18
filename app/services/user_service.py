from ..models import User as UserModel
from ..models import PlanType
from .template_service import TemplateService

class ErrorUser(Exception):
    """Base class for exceptions in this module."""
    pass

class UserWithSameEmailError(ErrorUser):
    """Exception raised when trying to register with an email that has already been used."""
    pass

class UserWithSameNumberError(ErrorUser):
    """Exception raised when trying to register with an phone number that has already been used."""
    pass

class WrongCredentialsError(ErrorUser):
    """Exception raised when wrong credentials has been provided."""
    pass


class UserService:

    @staticmethod
    def insert(user_info):
        user = UserService.create(user_info)
        return UserService.add(user)

    @staticmethod
    def create(user_info):
        user =  UserModel(nom = user_info["nom"],
                     phone_number = user_info["phone_number"],
                     email = user_info["email"])
        return user

    @staticmethod
    def add(user, plan_type=PlanType.STANDARD):
        UserModel.insert(user)
        return user

    @staticmethod
    def add_template(template_info, creator_id):
        template_info['creator_id'] = creator_id
        template = TemplateService.create(template_info)
        template.save()
        user = UserService.get(creator_id)
        user.templates.append(template)
        user.save()
        return template

    @staticmethod
    def get(id):
        return UserModel.objects.with_id(id)

    @staticmethod
    def get_or(id, callback):
        user = UserService.get(id)
        if user == None:
            callback()
        return user

    @staticmethod
    def delete_or(id, callback):
        user = UserService.get(id)
        if user == None:
            callback()
        else:
            user.delete()

    @staticmethod
    def update_or(id, data, callback):
        user = UserService.get(id)
        if user == None:
            callback()
        else:
            user.update(data)

    @staticmethod
    def get_list():
        return UserModel.objects()

    @staticmethod
    def count():
        return UserModel.objects.count()

    @staticmethod
    def get_id(token):
        return UserModel.decode_auth_token(token)

    @staticmethod
    def login(login_info):
        user = UserModel.objects(email=login_info['email']).first()
        if user == None:
            raise WrongCredentialsError()
        if not user.check_password(login_info['password']):
            raise WrongCredentialsError()
        return user.encode_auth_token()

    @staticmethod
    def register(user_info):
        user_with_email = UserModel.objects(email=user_info['email']).first()
        if user_with_email:
            raise UserWithSameEmailError()

        user_with_phone_number = UserModel.objects(phone_number=user_info['phone_number']).first()
        if user_with_phone_number:
            raise UserWithSameNumberError()

        user =  UserService.create(user_info)
        user.set_password(user_info["password"])
        UserService.add(user)
        return user, user.encode_auth_token()

    @staticmethod
    def register_admin(user_info):
        user, auth_token = UserService.register(user_info)
        user.set_admin()
        return user, auth_token
