import random
random.seed(16)

class CheckingAccount:
    def __init__(self):
        self._balance = 0
        self.account_number = str(random.randint(1000, 2000))
        self.account_type = 'Checking'

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance += value


class SavingAccount:
    def __init__(self):
        self._balance = 0
        self.account_number = str(random.randint(2000, 3000))
        self.account_type = 'Saving'

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance += value

