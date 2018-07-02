# -*- coding: utf-8 -*-


class JsonParser:
    def __init__(self, json, model):
        self.json = json
        self.model = model

    def __find_field(self, field, json):
        value = 0
        for (key, val) in json:
            if (key == field):
                value = val
            elif type(val) == dict:
                value = self.__find_field()
        return value


    def find_all_fileds(self, fields):
        for field in fields:
            self.__find_field()
        return 0

    def json_to_database(self):
        name = self.model.__name__
        model_fileds = self.model._meta.get_fields()
        serialized = {
            "model": name,
            "fields": {
                "name": "Mostly Harmless",
                "author": 42
            }
        }

        print(model_fileds)
        # person, created = self.model.objects.get_or_create(identifier=id)
