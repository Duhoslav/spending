# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, help_text="Название категории")

    def __str__(self):
        return self.name


class Check(models.Model):
    fiscalDocumentNumber = models.IntegerField(primary_key=True, help_text="ФПД", default=0)
    dateTime = models.CharField(max_length=200, help_text="Время покупки", default="")
    user = models.TextField(max_length=200, help_text="Организация", default="")
    retailPlaceAddress = models.CharField(max_length=500, help_text="Адрес магазина", default="")
    totalSum = models.IntegerField(help_text="Сумма по чеку в копеках", default=0)

    def __str__(self):
        return self.dateTime


class Item(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.FloatField(blank=True)
    sum = models.IntegerField(help_text="Цена в копейках")
    producer = models.CharField(max_length=500, blank=True)
    category = models.ForeignKey(Category, blank=True, on_delete=None, null=True)
    cash_check = models.ForeignKey(Check, on_delete=None)

    def __str__(self):
        return self.name
