import abc
from validators import PositiveNumberValidator


class Transaction(abc.ABC):
    @abc.abstractmethod
    def execute(self):
        ...


class DepositTransaction(Transaction):
    amount = PositiveNumberValidator()

    def __init__(self, account, amount):
        self.account = account
        self.amount = amount
        self.transaction_type = 'Deposit'

    def execute(self):
        self.account.deposit(self.amount)
        self.account.add_transaction(self)


class WithdrawTransaction(Transaction):
    amount = PositiveNumberValidator()

    def __init__(self, account, amount):
        self.account = account
        self.amount = amount
        self.transaction_type = 'Withdraw'

    def execute(self):
        self.account.withdraw(self.amount)
        self.account.add_transaction(self)


class TransferTransaction(Transaction):
    amount = PositiveNumberValidator()

    def __init__(self, debit_account, credit_account, amount):
        self.debit_account = debit_account
        self.credit_account = credit_account
        self.amount = amount
        self.transaction_type = 'Transfer'

    def execute(self):
        self.debit_account.withdraw(self.amount)
        self.credit_account.deposit(self.amount)
        self.debit_account.add_transaction(self)
        self.credit_account.add_transaction(self)




