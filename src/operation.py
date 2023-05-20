from dataclasses import dataclass


@dataclass
class Operation:

    """ Класс Operation, хранит информацию по банковской операции.

    Attributes
    ----------
    id_ - id транзакции
    date_ - информация о дате совершения банковской операции
    state - статус перевода
    sum_ - сумма банковской операции
    currency - валюта банковской операции
    description - описание типа перевода
    from_ - откуда (источник)
    to - куда (назначение)
    """

    id_: str
    date_: str
    state: str
    sum_: str
    currency: str
    description: str
    from_: str
    to: str

    def get_date(self):
        """ Возвращает дату операции. """
        return self.date_

    def get_description(self):
        """ Возвращает описание перевода. """
        return self.description

    def get_state(self):
        """ Возвращает статус операции: EXECUTED или CANCELED. """
        return self.state

    def get_from(self):
        """ Возвращает откуда перевод или оплата. """
        return self.from_

    def get_to(self):
        """ Возвращает куда ушел перевод или оплата. """
        return self.to
