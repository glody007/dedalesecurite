from ..models import Template as TemplateModel

class ErrorTemplate(Exception):
    """Base class for exceptions in this module."""
    pass

class TemplateNotFoundError(Exception):
    """Exception raised if template not found in db."""
    pass

def template_not_found():
    raise TemplateNotFoundError()

class TemplateService:

    @staticmethod
    def insert(template_info):
        template = TemplateService.create(template_info)
        return TemplateService.add(template)

    @staticmethod
    def create(template_info):
        template =  TemplateModel(nom = template_info["nom"],
                                  document_model = template_info["document_model"],
                                  datas_model = template_info["datas_model"],
                                  creator_id = template_info["creator_id"])
        return template

    @staticmethod
    def add(template):
        return template.save()

    @staticmethod
    def get(id):
        return TemplateModel.objects.with_id(id)

    @staticmethod
    def get_or(id, callback):
        template = TemplateService.get(id)
        if template == None:
            callback()
        return template

    @staticmethod
    def delete_or(id, callback):
        template = TemplateService.get(id)
        if template == None:
            callback()
        else:
            template.delete()

    @staticmethod
    def update_or(id, data, callback):
        template = TemplateService.get(id)
        if template == None:
            callback()
        else:
            template.update(data)

    @staticmethod
    def get_list():
        return TemplateModel.objects()

    @staticmethod
    def count():
        return TemplateModel.objects.count()