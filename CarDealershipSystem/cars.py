from abc import ABC, abstractmethod
from typing import Union
from validators import *


class Car(ABC):
    @abstractmethod
    def show_expense(self, price: Union[int, float]) -> Union[int, float]:
        ...


class ElectricCar(Car):
    make = StringValidator()
    model = StringValidator()
    price = PositiveNumberValidator()

    def __init__(self, make: str, model: str, price: Union[int, float]) -> None:
        self.make = make
        self.model = model
        self.price = price
        self.type = 'Electric'

    def show_expense(self, price: Union[int, float]) -> Union[int, float]:
        '''Method returns expense per 100km.'''
        return price * 100

    def __repr__(self):
        return f'make: {self.make}, model: {self.model}, price: {self.price}'

    def copy(self):
        new_instance = ElectricCar(make=self.make, model=self.model, price=self.price)
        return new_instance


class PetrolCar(Car):
    make = StringValidator()
    model = StringValidator()
    price = PositiveNumberValidator()

    def __init__(self, make: str, model: str, price: Union[int, float]) -> None:
        self.make = make
        self.model = model
        self.price = price
        self.type = 'Petrol'

    def show_expense(self, price: Union[int, float]) -> Union[int, float]:
        '''Method returns expense per 100km.'''
        return price * 100

    def __repr__(self):
        return f'make: {self.make}, model: {self.model}, price: {self.price}'

    def copy(self):
        new_instance = ElectricCar(make=self.make, model=self.model, price=self.price)
        return new_instance


class HybridCar(Car):
    make = StringValidator()
    model = StringValidator()
    price = PositiveNumberValidator()

    def __init__(self, make: str, model: str, price: Union[int, float]) -> None:
        self.make = make
        self.model = model
        self.price = price
        self.type = 'Hybrid'

    def show_expense(self, price: Union[int, float]) -> Union[int, float]:
        '''Method returns expense per 100km.'''
        return price * 100

    def __repr__(self):
        return f'make: {self.make}, model: {self.model}, price: {self.price}'

    def copy(self):
        new_instance = ElectricCar(make=self.make, model=self.model, price=self.price)
        return new_instance

