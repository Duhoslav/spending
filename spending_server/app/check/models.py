# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, help_text="Название категории")

    def __unicode__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=200)
    count = models.IntegerField()
    price = models.IntegerField(help_text="Цена в копейках")
    producer = models.CharField(max_length=500)
    category = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name


class Check(models.Model):
    fiscalDocumentNumber = models.IntegerField(primary_key=True, help_text="ФПД", default=0)
    dateTime = models.CharField(max_length=200, help_text="Время покупки", default="")
    user = models.TextField(max_length=200, help_text="Организация", default="")
    retailPlaceAddress = models.CharField(max_length=500, help_text="Адрес магазина", default="")
    totalSum = models.IntegerField(help_text="Сумма по чеку в копеках", default=0)

    def __unicode__(self):
        return self.dateTime
