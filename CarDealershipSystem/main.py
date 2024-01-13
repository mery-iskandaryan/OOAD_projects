from cars import *
from salespeople import Salesman
from customers import Customer
from sales_operations import *
salesman = []

if __name__ == '__main__':
    salesman1 = Salesman("Bob", 5.5)
    salesman2 = Salesman("Joe", 4)
    car1 = ElectricCar('Tesla', 'ModelY', 40000)
    car2 = PetrolCar('Mercedes', 'E-class', 25000)
    car3 = HybridCar('Toyota', 'Camry', 7000)
    salesman1.add_car(car1)
    salesman1.add_car(car2)
    salesman2.add_car(car1)
    salesman2.add_car(car2)
    salesman2.add_car(car3)
    salesman.append(salesman1)
    salesman.append(salesman2)

    customer1 = Customer('James', '77785999')

    car_to_buy = customer1.search_car('Mercedes', 'E-class', salesman)

    print(car_to_buy)
    purchase = PurchaseCar(salesman1, customer1, car_to_buy)
    purchase.execute()
    salesman1.view_inventory_history()

