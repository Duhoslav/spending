# -*- coding: utf-8 -*-
import requests


def check_valid(fn, fd, fp):
    try:
        url = 'https://proverkacheka.nalog.ru:9999/v1/ofds/*/inns/*/fss/{0}/operations/1/tickets/{1}?fiscalSign={2}&date=2018-06-18T20:56:00&sum=25329'.format(
            fn, fd, fp)
        response = requests.get(url)
        print(response.status_code, response.reason)
        print(response.text[:300] + '...')
        return (response.json())
    except Exception as e:
        print(e)


def get_check(login, password, fn, fd, fp):
    try:
        url = 'https://proverkacheka.nalog.ru:9999/v1/inns/*/kkts/*/fss/{0}/tickets/{1}?fiscalSign={2}&sendToEmail=no'.format(
            fn, fd, fp)
        header = {"Device-Id": "12345", "Device-OS": "Android 5.1"}
        response = requests.get(url, auth=(login, password), headers=header)
        print(response.status_code, response.reason)
        print(response.json())
        return (response.json())
    except Exception as e:
        print(e)
