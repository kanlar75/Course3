import json

import pytest

from src.operation import Operation

""" 
Экземпляры класса Operation для тестирования: 'obj_full' - все атрибуты, 
'obj_no_full' - поле 'from' отсутствует, obj_canceled - статус 'CANCELED'.
"""


@pytest.fixture
def obj_full_attributes():
    obj_full = Operation("41428829", "2019-07-03T18:35:29.512364", "EXECUTED",
                         "8221.37", "USD", "Перевод организации",
                         "MasterCard 7158300734726758",
                         "Счет 35383033474447895560")
    return obj_full


@pytest.fixture
def obj_no_full_attributes():
    obj_no_full = Operation('172864002', "2018-12-28T23:10:35.459698",
                            "EXECUTED", "49192.52", "USD", "Открытие вклада",
                            "", "Счет 96231448929365202391")
    return obj_no_full


@pytest.fixture
def obj_canceled_attributes():
    obj_canceled = Operation("121646999", "2018-06-08T16:14:59.936274",
                             "CANCELED",
                             "91121.62", "руб.", "Перевод организации",
                             "Maestro 7552745726849311",
                             "Счет 34799481846914116850")
    return obj_canceled


@pytest.fixture
def suspend_capture(pytestconfig):
    """ Для тестирования функции input_int('text'), ввод с клавиатуры. """

    class suspend_guard:
        def __init__(self):
            self.capmanager = pytestconfig.pluginmanager.getplugin(
                'capturemanager')

        def __enter__(self):
            self.capmanager.suspend_global_capture(in_=True)

        def __exit__(self, _1, _2, _3):
            self.capmanager.resume_global_capture()

    yield suspend_guard()


@pytest.fixture(scope='module')
def json_data():

    """ Содержит данные json для тестов. """
    json_ = [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 172864002,
            "state": "EXECUTED",
            "date": "2018-12-28T23:10:35.459698",
            "operationAmount": {
                "amount": "49192.52",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 96231448929365202391"
        },
        {
            "id": 121646999,
            "state": "CANCELED",
            "date": "2018-06-08T16:14:59.936274",
            "operationAmount": {
                "amount": "91121.62",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 7552745726849311",
            "to": "Счет 34799481846914116850"
        },
        {},
        {"id": 736942989,
         "state": "EXECUTED",
         "date": "2019-09-06T00:48:01.081967",
         "operationAmount": {
             "amount": "6357.56",
             "currency": {
                 "name": "USD",
                 "code": "USD"
             }
         },
         "description": "Перевод организации",
         "from": "Visa Gold 3654412434951162",
         "to": "Счет 59986621134048778289"
         },
        {
            "id": 580054042,
            "state": "EXECUTED",
            "date": "2018-06-20T03:59:34.851630",
            "operationAmount": {
                "amount": "96350.51",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "МИР 3766446452238784",
            "to": "Счет 86655182730188443980"
        }
    ]
    return json_


@pytest.fixture(scope='module')
def temp_file_json(tmpdir_factory, json_data):
    """
    Записываем тестовые данные в файл 'test.json' во временной
    директории.
    """
    temp_data = json_data
    file = tmpdir_factory.mktemp('data').join('test.json')

    with file.open('w') as f:
        json.dump(temp_data, f)
    return file
