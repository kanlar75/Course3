import json

from datetime import datetime

from src.operation import Operation

file_name = "operations.json"


def int_input(text):
    """
    Проверяет введено ли пользователем число, если нет, то в цикле просим
    ввести число.
    """

    while True:
        try:
            num = int(input(text))
        except ValueError:
            print("Нужно ввести ЧИСЛО операций")
        else:
            return num


def load_data(path=file_name):
    """ Получает данные банковских операций из файла json. """

    try:
        with open(path, 'r', encoding='utf-8') as file:
            operations = json.load(file)
        return operations
    except FileNotFoundError:
        print(f'Файл с банковскими операциями "{path}" отсутствует! ')
        return []


def make_instances():
    """
    Возвращает список экземпляров класса Operation с успешным статусом
    'EXECUTED'. Данные считываются из файла и раскладываются в экземпляры
    класса Operation. Все экземпляры добавляются в список, который сортируется
    по убыванию даты.
    """
    operations = load_data()
    operations_list = []
    field = 'operationAmount'

    for operation in operations:
        if len(operation) > 0:
            if operation.get('state').strip().lower() != "canceled":
                obj = Operation(str(operation.get('id')),
                                operation.get('date'),
                                operation.get('state'),
                                operation.get(field, {}).get('amount'),
                                operation.get(field, {}).get('currency', {}).
                                get('name'),
                                operation.get('description'),
                                operation.get('from', ""),
                                operation.get('to'))
            else:
                continue
        else:
            continue
        operations_list.append(obj)
        operations_list.sort(key=lambda lst_: lst_.date_, reverse=True)
    return operations_list


def get_date(operation):
    """
    Получает дату из экземпляра класса Operation, возвращает в формате
    ДД.ММ.ГГГГ.
    """

    date_ = datetime.strftime(datetime.fromisoformat(operation.date_),
                              '%d.%m.%Y')
    return date_


def get_operation_amount(operation):
    """ Возвращает сумму и валюту операции. """

    sum_ = operation.sum_
    currency = operation.currency
    return f'{sum_} {currency}'


def get_from_to(operation):
    """ Возвращает строку по операции откуда и куда. """

    list_t = operation.to.split()
    if operation.from_ == "":
        return f' --> {hide_numbers(list_t)}'
    list_f = operation.from_.split()
    return f'{hide_numbers(list_f)} --> {hide_numbers(list_t)}'


def hide_numbers(list_):
    """ Определяет счет или карта. Маскирует номер. """

    view = ''
    text = []

    for element in list_:
        if element.isdigit():
            if len(element) == 20:
                view = f'**{element[-4:]}'
            elif len(element) == 16:
                view = f'{element[0:4]} {element[4:6]}** **** {element[-4:]}'
        else:
            text.append(element)
    return f'{" ".join(text)} {view}'

