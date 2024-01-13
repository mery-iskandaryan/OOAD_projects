from typing import Union
from validators import *
from inventory import Inventory
from cars import Car


class Salesman:
    name = StringValidator()
    commission_rate = PositiveNumberValidator()

    def __init__(self, name: str, commission_rate: Union[int, float]) -> None:
        self.name = name
        self.commission_rate = commission_rate
        self.inventory = Inventory()
        self.history = f'{self.name}\'s inventory history:\n'

    def add_car(self, car) -> None:
        new_car = car.copy()
        new_car.price = car.price * ((self.commission_rate/100) + 1)
        self.history += f'{car.make} {car.model} added to inventory with price {car.price}.\n'
        self.inventory.add_car(new_car)

    def remove_car(self, car) -> None:
        self.inventory.remove_car(car)
        self.history += f'{car.make} {car.model} sold from inventory with price {car.price}.\n'

    def view_inventory_history(self):
        print(self.history)
