import json

from src.utils import load_data, get_date, get_operation_amount, get_from_to, \
    hide_numbers, make_instances, int_input


def test_load_data_bad():
    """
    Пробуем считывать данные из несуществующего файла, получаем пустой
    список и сообщение, что файл отсутствует.
    """

    assert load_data("bad.json") == []


def test_load_data_good(temp_file_json):
    """
    Считываем данные из тестового файла json. Проверяем что функция
    load_data считывает данные аналогично json.load().
    """

    assert json.load(temp_file_json) == load_data(temp_file_json)


def test_make_instance(temp_file_json, obj_canceled_attributes):
    """
    Создаем список экземпляров из тестового файла json, проверяем
    присутствует ли в нем тестовый экземпляр со статусом 'CANCELED'
    """

    load_data(temp_file_json)

    assert obj_canceled_attributes not in make_instances(temp_file_json)


def test_get_date(obj_full_attributes):
    """ Получаем дату у экземпляра, сравниваем с ожидаемой датой. """

    assert get_date(obj_full_attributes) == "03.07.2019"


def test_get_operation_amount(obj_full_attributes):
    """ Получаем сумму и валюту операции, сравниваем с ожидаемыми. """

    assert get_operation_amount(obj_full_attributes) == "8221.37 USD"


def test_get_from_to_full(obj_full_attributes):
    """
    Получаем источник и назначение операции у тестового экземпляра с
    полными атрибутами, сравниваем с ожидаемыми.
    """

    assert get_from_to(obj_full_attributes) == "MasterCard 7158 30** **** " \
                                               "6758 " \
                                               "--> Счет **5560"


def test_get_from_to_no_full(obj_no_full_attributes):
    """
    Получаем источник и назначение операции у тестового экземпляра с
    неполными атрибутами, отсутствует 'from'сравниваем с ожидаемыми.
    """

    assert get_from_to(obj_no_full_attributes) == " --> Счет **2391"


def test_hide_numbers_full():
    """
    Передаем на вход список, который формируется в get_from_to, смотрим
    как происходит маскировка номера карты или счета. Подаем разные значения
    номера, видим, что если номер не 16 или 20 цифрБ то возвращается пустая
    строка. Если номер содержит 16 или 20 цифр, возвращается карта или счет.
    """

    assert hide_numbers(["Счет", "35383033474447895560"]) == "Счет **5560"
    assert hide_numbers(["MasterCard", "5678912345678911"]) == \
           "MasterCard 5678 91** **** 8911"
    assert hide_numbers(["MasterCard", "91211"]) == "MasterCard "
    assert hide_numbers([]) == " "


def test_int_input(suspend_capture):
    """
    Сначала ввести букву или символ, дождаться сообщения 'Нужно ввести
    ЧИСЛО операций', затем ввести число.
    """

    with suspend_capture:
        number = int_input("Введите число операций для просмотра, ""\n--->  ")
    assert isinstance(number, int)
