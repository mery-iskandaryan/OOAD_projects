import cars
import salespeople
import customers

car1 = cars.Car('Mercedes', 'E-class', 8000)
car2 = cars.Car('Tesla', 'ModelY', 60000)
car3 = cars.Car('Toyota', 'Corolla', 9000)

salesman1 = salespeople.Salesperson('Bob', 10.5)
salesman1.add_car(car1)
salesman1.add_car(car2)

salesman2 = salespeople.Salesperson('Jack', 9.5)
salesman2.add_car(car2)

salesman3 = salespeople.Salesperson('Daniel', 8)
salesman3.add_car(car3)


c1 = customers.Customer('Mery', '7858999')
c1.purchase_car('Tesla', 'ModelY')

print(salesman2.sales_history)
c1.purchase_car('Toyota', 'Corolla')


