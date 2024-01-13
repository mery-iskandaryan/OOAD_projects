from cars import Car


class Inventory:
    def __init__(self):
        self.car_list = []

    def add_car(self, car: Car):
        self.car_list.append(car)

    def remove_car(self, car: Car):
        self.car_list.remove(car)
