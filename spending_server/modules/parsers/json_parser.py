# -*- coding: utf-8 -*-


class JsonParser:
    def __init__(self, json, models):
        self.json = json
        self.models = models

    def __get_field_by_key(self, field, json, result):
        for (key, val) in json.items():
            if key == field:
                result.append(val)
            elif type(val) == dict:
                self.__get_field_by_key(field, val, result)
            elif type(val) == list and len(val) > 0:
                for item in val:
                    if type(item) == dict:
                        self.__get_field_by_key(field, item, result)

    def find_all_fields(self, fields):
        result = {}
        for field in fields:
            values = []
            self.__get_field_by_key(field, self.json, values)
            if len(values) > 0:
                result[field] = values
        return result

    def json_to_database(self):
        serialized = []
        for model in self.models:
            name = model._meta.label
            model_fields = model._meta.get_fields()
            model_fields = [x.attname for x in model_fields if hasattr(x, 'attname')]
            fields = self.find_all_fields(fields=model_fields)
            object_count = max([len(v) for (k, v) in fields.items()])
            for i in range(object_count):
                new_fields = {}
                for (key, val) in fields.items():
                    new_fields[key] = val[i]
                serialized.append({
                    "model": name,
                    "fields": new_fields
                })
        return serialized
