from validators import StringValidator
from typing import List
from cars import *
from sales_operations import *


class Customer:
    name = StringValidator()

    def __init__(self, name: str, phone_number: str):
        self.name = name
        self.phone_number = phone_number
        self.cars = []

    def search_car(self, make: str, model: str, salespeople: List) -> Union[Car, str]:
        for salesman in salespeople:
            for car in salesman.inventory.car_list:
                if car.make == make and car.model == model:
                    return car
        raise ValueError('The searched car is not present in inventory.')

    def purchase_car(self, car: Car) -> None:
        self.cars.append(car)

    # def purchase_car(self, salespeople: List) -> None:
    #     car_list = {}
    #     for salesman in salespeople:
    #         print(f'{salesman.name}: {[car for car in salesman.inventory.car_list]}')
    #         car_list[salesman.name] = (salesman, [car for car in salesman.inventory.car_list])
    #     chosen_salesman = input("Choose the salesman (Enter the salesman name): ")
    #     chosen_car = input("Choose the car (Enter the car model): ")
    #     for salesman in salespeople:
    #         if salesman.name == chosen_salesman:
    #             for car in car_list[salesman]:
    #                 if car.model == chosen_car:
    #                     self.cars.append(car)
    #                     salesman.remove_car(car)
    #                     print(f'Congratulations, you have just bought {car.make} {car.model} with {car.price} USD.')

