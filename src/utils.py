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
