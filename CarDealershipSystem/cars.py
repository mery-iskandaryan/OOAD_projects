class Car:
    def __init__(self, make: str, model: str, price: int):
        self.make = make
        self.model = model
        self.price = price

    def __str__(self):
        return f'make: {self.make}, model: {self.model}, price: {self.price}'


class ElectricCar(Car):
    def __init__(self, make: str, model: str, price: int):
        super().__init__(make, model, price)
        self.car_type = 'Electric'


class HybridCar(Car):
    def __init__(self, make: str, model: str, price: int):
        super().__init__(make, model, price)
        self.car_type = 'Hybrid'


class PetrolCar(Car):
    def __init__(self, make: str, model: str, price: int):
        super().__init__(make, model, price)
        self.car_type = 'Petrol'
