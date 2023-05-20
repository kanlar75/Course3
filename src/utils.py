import json

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

