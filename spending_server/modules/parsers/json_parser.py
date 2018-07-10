# -*- coding: utf-8 -*-

class JsonParser:
    def __init__(self, json, model):
        self.json = json
        self.model = model

    def __get_value_by_key(self, field, json):
        value = 0
        for (key, val) in json.items():
            if key == field:
                value = val
            elif type(val) == dict:
                value = self.__get_value_by_key(field, val)
        # if value.isdigit():
        #     value = int(value)
        return value

    def find_all_fileds(self, fields):
        result = {}
        for field in fields:
            val = self.__get_value_by_key(field, self.json)
            if val != 0:
                result[field] = val
        return result

    def json_to_database(self):
        name = self.model._meta.label
        model_fileds = self.model._meta.get_fields()
        #model_fileds[0].attname
        model_fileds = [x.attname for x in model_fileds]
        fields = self.find_all_fileds(fields=model_fileds)
        serialized = {
            "model": name,
            "fields": fields
        }
        return serialized
        # person, created = self.model.objects.get_or_create(identifier=id)
