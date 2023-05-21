def main():
    from src.utils import int_input, get_date, get_from_to, \
        get_operation_amount, make_instances

    # Создаем список экземпляров класса Operation с успешными операциями,
    # который отсортирован в порядке убывания по дате операции
    operations = make_instances()

    # Если список экземпляров не пустой
    if len(operations) != 0:

        # Предлагаем пользователю ввести число операций для просмотра
        number_operations = int_input(
            'Введите число операций для просмотра \n---> ')

        # Проверяем не ввел ли пользователь желаемое число операций больше,
        # чем в файле с банковскими операциями. Если желает увидеть больше
        # чем есть, покажем все.

        if number_operations <= len(operations):
            message = ""
        else:
            number_operations = len(operations)
            message = f"\nПоказаны все {len(operations)} успешных операций\n"

        # Цикл вывода информации по запрошенным операциям
        for i in range(number_operations):
            print(f'\n{get_date(operations[i])} {operations[i].description}')
            print(f'{get_from_to(operations[i])}')
            print(f'{get_operation_amount(operations[i])}')
        print(f'{message}')
    else:
        # Список экземпляров пустой, т.к. отсутствует файл с банковскими
        # операциями, или все операции не успешные

        print("Нет информации для просмотра!")


if __name__ == '__main__':
    main()
