from django.shortcuts import render, get_object_or_404, redirect
from modules import network
from modules.parsers import json_parser
from app.check.models import Check


################################
#### API Method to get check. Creds required.
###############################
def get_check(request):
    context = {
        "check": 'qwe'
    }
    return render(request, 'check.html', context=context)


def add_check(request):
    print('ok')
    json = network.get_cash()
    parser = json_parser.JsonParser(json=json, model=Check)
    res = parser.json_to_database()
    return render(request, 'check.html')
