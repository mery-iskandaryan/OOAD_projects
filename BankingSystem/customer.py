import account
import transaction


class Customer:
    customers = []

    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.accounts = {}
        Customer.customers.append(self)

    def create_account(self, account_type):
        if account_type == 'Checking':
            new_account = account.CheckingAccount()
            self.accounts[new_account.account_number] = new_account

        elif account_type == 'Saving':
            new_account = account.SavingAccount()
            self.accounts[new_account.account_number] = new_account

        elif account_type == 'Both':
            new_account1 = account.CheckingAccount()
            new_account2 = account.SavingAccount()
            self.accounts[new_account1.id] = new_account1
            self.accounts[new_account2.id] = new_account2

    def deposit(self, amount: int, account_number: str) -> None:
        transaction.Transaction().deposit(amount=amount, credit_account=self.accounts[account_number])

    def withdrawal(self, amount: int, account_number: str) -> None:
        if self.accounts[account_number].balance < amount:
            raise ValueError("Not enough balance...")
        transaction.Transaction().withdrawal(amount = amount, debit_account=self.accounts[account_number])

    def money_transfer(self, amount: int, debit_account: 'Account', credit_account: str) -> None:
        if self.accounts[debit_account].balance < amount:
            raise ValueError("Not enough balance...")
        for customer in Customer.customers:
            if credit_account in customer.accounts:
                credit_account = customer.accounts[credit_account]
                break
        transaction.Transaction().money_transfer(amount, self.accounts[debit_account], credit_account)

    def __str__(self):
        return f"name: {self.name}, contact: {self.contact_info}, accounts: {[account for account in self.accounts]}"

