from ..models import User as UserModel
from ..models import PlanType


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
            user.update_from_info(data)

    @staticmethod
    def get_list():
        return UserModel.objects()

    @staticmethod
    def count():
        return UserModel.objects.count()

    @staticmethod
    def register(user_info):
        user =  UserService.create(user_info)
        user.set_password(user_info["password"])
        UserService.add(user)
        return user

    @staticmethod
    def register_admin(user_info):
        user = UserModel.objects(email=user_info["email"]).first()
        if user == None:
            user = UserService.register(user_info)
            user.set_admin()
        return user
