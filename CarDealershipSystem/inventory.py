class Inventory:
    def __init__(self):
        self.inventory = []

    def add_car(self, car: 'Car') -> None:
        self.inventory.append(car)

    def remove_car(self, car: 'Car') -> None:
        self.inventory.remove(car)

    def search_car(self, car_make: str, car_model: str) -> 'Car':
        for car in self.inventory:
            if car.make == car_make and car.model == car_model:
                return car

    def __str__(self):
        return str([f"car_make: {car.make}, car_model: {car.model}, car_price: {car.price}" for car in self.inventory])



