from ..models import Datas as DatasModel

class ErrorDatas(Exception):
    """Base class for exceptions in this module."""
    pass

class DatasNotFoundError(Exception):
    """Exception raised if datas not found in db."""
    pass

def datas_not_found():
    raise DatasNotFoundError()

class DatasService:

    @staticmethod
    def insert(datas_info):
        datas = DatasService.create(datas_info)
        return DatasService.add(datas)

    @staticmethod
    def create(datas_info):
        datas =  DatasModel(values = datas_info["values"],
                            template_id = datas_info["template_id"])
        return datas

    @staticmethod
    def add(datas):
        return datas.save()

    @staticmethod
    def get(id):
        return DatasModel.objects.with_id(id)

    @staticmethod
    def get_or(id, callback):
        datas = DatasService.get(id)
        if datas == None:
            callback()
        return datas

    @staticmethod
    def delete_or(id, callback):
        datas = DatasService.get(id)
        if datas == None:
            callback()
        else:
            datas.delete()

    @staticmethod
    def update_or(id, data, callback):
        datas = DatasService.get(id)
        if datas == None:
            callback()
        else:
            datas.update(data)

    @staticmethod
    def get_list(template_id=None):
        return DatasModel.objects()

    @staticmethod
    def count():
        return DatasModel.objects.count()
