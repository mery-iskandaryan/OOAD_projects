from customers import Customer
from accounts import CheckingAccount, SavingAccount
import transactions


if __name__ == '__main__':
    try:
        customer1 = Customer('Mery', '785999')
        account1 = CheckingAccount()
        account2 = SavingAccount(100000)

        customer1.add_account(account1)
        customer1.add_account(account2)
        # print(customer1.list_accounts())
        deposit = transactions.DepositTransaction(account1, 100000)
        deposit.execute()
        transfer = transactions.TransferTransaction(account1, account2, 50000)
        transfer.execute()
        # customer1.list_accounts()
        withdraw = transactions.WithdrawTransaction(account2, 60000)
        # withdraw.execute()

        for account in customer1.list_accounts():
            print(account.view_transaction_history())

    except ValueError as e:
        print(e)
