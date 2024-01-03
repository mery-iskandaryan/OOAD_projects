import customer

c1 = customer.Customer('Bob', '785999')
c1.create_account('Saving')
c1.create_account('Saving')

c2 = customer.Customer('James', '878555')
c2.create_account('Checking')

print(c1)
print(c2)

c1.deposit(3000, '2370')
c2.deposit(1000, '1492')
print(c1.accounts['2370'].balance)
print(c2.accounts['1492'].balance)
c1.money_transfer(2000, '2370', '1492')
print(c2.accounts['1492'].balance)
