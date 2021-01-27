"""
1. Инкапсуляция — это способность объектов скрывать часть
своего состояния и поведения от других объектов, предоставляя внешнему миру только определённый интерфейс
взаимодействия с собой.
"""
class BankAccount:
    name = 'Aidar'  # public
    _passport = 'AN203832'  # protected / public
    __balance = 0  # private

    def get_balance(self):
        return self.__balance

    def __get_passport(self):
        return self._passport
account = BankAccount()
print(account.name, account._passport, account.get_balance())
