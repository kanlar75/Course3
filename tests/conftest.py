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
    class suspend_guard:
        def __init__(self):
            self.capmanager = pytestconfig.pluginmanager.getplugin(
                'capturemanager')

        def __enter__(self):
            self.capmanager.suspend_global_capture(in_=True)

        def __exit__(self, _1, _2, _3):
            self.capmanager.resume_global_capture()

    yield suspend_guard()

