from validators import StringValidator
from typing import List


class Customer:
    name = StringValidator()

    def __init__(self, name: str, phone_number: str):
        self.name = name
        self.phone_number = phone_number
        self.accounts = {}

    def add_account(self, account: 'Account') -> None:
        self.accounts[account.account_number] = account

    def get_account(self, account_number: 'str') -> 'Account':
        return self.accounts.get(account_number)

    def list_accounts(self) -> List[str]:
        return list(self.accounts.values())


