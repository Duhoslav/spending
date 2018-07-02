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
    id = models.CharField(max_length=32, primary_key=True)
    ts = models.CharField(max_length=200)
    organization = models.TextField(max_length=200)
    address = models.CharField(max_length=500)
    cash_total_sum = models.IntegerField(help_text="Сумма по чеку в копеках")

    def __unicode__(self):
        return self.ts