from django.shortcuts import render, get_object_or_404, redirect
from modules import network
from modules.parsers import json_parser
from app.check.models import Check, Item
from django.core import serializers

################################
#### API Method to get check. Creds required.
###############################
def get_check(request):
    context = {
        "check": "qwe"
    }
    return render(request, "check.html", context=context)


def add_check(request):
    print("ok")
    # model = serializers.serialize(Check.objects.all())
    json = network.get_cash()
    parser = json_parser.JsonParser(json=json, models=(Check, Item))
    serialized_check = parser.json_to_database()
    check_object = None
    for deserialized_object in serializers.deserialize("python", serialized_check):
        if deserialized_object.object._meta.model_name == 'check':
            check_object = deserialized_object.object
        elif deserialized_object.object._meta.model_name == 'item':
            deserialized_object.object.cash_check = check_object
        deserialized_object.save()
    return render(request, "check.html")
