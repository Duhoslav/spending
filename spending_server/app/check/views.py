from django.shortcuts import render
from app.check.models import Check, Category, Item
from modules import network
from modules.parsers import json_parser


def check(request):
    checks = Check.objects.all()
    context = {
        "checks": checks
    }
    return render(request, 'check.html', context=context)


def add_check(request):
    print('ok')
    #json = network.get_cash()
    #parser = json_parser.JsonParser(json=json, model=Check)
    #res = parser.json_to_database()
    return 0#render(request, 'check.html')