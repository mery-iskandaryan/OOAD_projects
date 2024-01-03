class Transaction:
    def deposit(self, amount, credit_account):
        credit_account.balance = credit_account.balance + amount

    def withdrawal(self, amount, debit_account: 'Account') -> None:
        if amount > debit_account.balance:
            raise ValueError("Not enough funds")
        debit_account.balance -= amount

    def money_transfer(self, amount: int, debit_account: 'Account', credit_account: 'Account') -> None:
        if debit_account.balance < amount:
            raise ValueError("Not enough funds")
        debit_account.balance -= amount
        credit_account.balance += amount
