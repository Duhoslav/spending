# -*- coding: utf-8 -*-


class JsonParser:
    def __init__(self, json, model):
        self.json = json
        self.model = model

    def json_to_database(self):
        model_fileds =  self.model._meta.get_fields()
        print(model_fileds)
        # person, created = self.model.objects.get_or_create(identifier=id)
