from abc import ABC, abstractmethod
from salespeople import Salesman
from cars import Car


class SalesOperations(ABC):
    @abstractmethod
    def execute(self):
        ...


class PurchaseCar(SalesOperations):
    def __init__(self, salesman: Salesman, buyer: 'Customer', car: Car) -> None:
        self.salesman = salesman
        self.customer = buyer
        self.car = car

    def execute(self):
        self.customer.purchase_car(self.car)
        self.salesman.remove_car(self.car)


class SellCar(SalesOperations):
    def __init__(self, salesman: Salesman, car: Car) -> None:
        self.salesman = salesman
        self.car = car

    def execute(self):
        self.salesman.remove_car(self.car)
