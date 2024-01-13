import abc
from typing import Union
import random
from validators import StringValidator, PositiveNumberValidator
random.seed(16)


class Account(abc.ABC):
    @abc.abstractmethod
    def deposit(self, amount: Union[int, float]) -> None:
        ...

    @abc.abstractmethod
    def withdraw(self, amount: Union[int, float]) -> None:
        ...

    @abc.abstractmethod
    def add_transaction(self, transaction):
        ...

    @abc.abstractmethod
    def view_transaction_history(self):
        ...


class CheckingAccount(Account):
    balance = PositiveNumberValidator()

    def __init__(self, balance=0):
        self.account_number = str(random.randint(2000, 3000))
        self.balance = balance
        self.transactions = []
        self.account_type = 'Checking'

    def deposit(self, amount: Union[int, float]) -> None:
        self.balance += amount

    def withdraw(self, amount: Union[int, float]) -> None:
        if amount > self.balance:
            raise ValueError(f'The amount of transaction must can\' be greater then the balance ({self.balance})')
        self.balance -= amount

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def view_transaction_history(self):
        res = f'Account Number: {self.account_number}, Account Type: {self.account_type}, Transactions: '
        ls = []
        for transaction in self.transactions:
            if transaction.transaction_type == 'Transfer':
                ls.append(f'Transaction Type: {transaction.transaction_type}, Receiver Account: {transaction.credit_account.account_number}, Amount: {transaction.amount}')
            ls.append(f'Transaction Type: {transaction.transaction_type}, Amount: {transaction.amount}')
        return res + str(ls)


class SavingAccount(Account):
    balance = PositiveNumberValidator()

    def __init__(self, balance=0):
        self.account_number = str(random.randint(3000, 4000))
        self.balance = balance
        self.transactions = []
        self.account_type = 'Saving'

    def deposit(self, amount: Union[int, float]) -> None:
        self.balance += amount

    def withdraw(self, amount: Union[int, float]) -> None:
        min_balance = 1000000
        if amount > self.balance:
            raise ValueError(f'The amount of transaction must can\' be greater then the balance ({self.balance})')
        if self.balance < min_balance:
            raise ValueError(f'The balance should be at least {min_balance} to be able to withdraw.')
        self.balance -= amount

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def view_transaction_history(self):
        res = f'Account Number: {self.account_number}, Account Type: {self.account_type}, Transactions: '
        ls = []
        for transaction in self.transactions:
            if transaction.transaction_type == 'Transfer':
                ls.append(f'Transaction Type: {transaction.transaction_type}, Sender Account: {transaction.debit_account.account_number}, '
                          f'Receiver Account: {transaction.credit_account.account_number}, Amount: {transaction.amount}')
            ls.append(f'Transaction Type: {transaction.transaction_type}, Amount: {transaction.amount}')
        return res + str(ls)


