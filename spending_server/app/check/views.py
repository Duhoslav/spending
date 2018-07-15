from django.shortcuts import render
from app.check.models import Check, Category, Item


def check(request):
    checks = Check.objects.all()
    goods = Item.objects.filter(cash_check__in=checks)
    context = {
        "checks": checks,
        "goods": goods
    }
    return render(request, "check.html", context=context)
