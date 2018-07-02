# -*- coding: utf-8 -*-


def get_cash():
    data = {
        "document": {
            "receipt": {
                "cashTotalSum": 0,
                "fiscalSign": 1301551154,
                "nds18": 4859,
                "operationType": 1,
                "userInn": "7728029110",
                "dateTime": "2018-05-18T22:05:00",
                "fiscalDocumentNumber": 12654,
                "receiptCode": 3,
                "ecashTotalSum": 97588,
                "nds10": 5976,
                "requestNumber": 395,
                "retailPlaceAddress": "г.Екатеринбург, ул.Сулимова, д.50",
                "fiscalDriveNumber": "871000010459859",
                "taxationType": 1,
                "user": "АО ТД Перекресток",
                "operator": "<Данные кассира>",
                "items": [
                    {
                        "sum": 3799,
                        "quantity": 1,
                        "price": 3799,
                        "name": "18074 Укроп пакет 100г",
                        "nds10": 345
                    },
                    {
                        "sum": 7490,
                        "quantity": 0.872,
                        "nds18": 1143,
                        "name": "2000339 Яблоки СЕЗОН.ПРЕДЛОЖЕНИЕ 1кг",
                        "price": 8590
                    }
                ],
                "totalSum": 97588,
                "shiftNumber": 262,
                "kktRegId": "0001248888049341"
            }
        }
    }
    return data
