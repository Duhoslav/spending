# Generated by Django 2.0.6 on 2018-07-11 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0002_auto_20180711_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=None, to='check.Category'),
        ),
    ]
