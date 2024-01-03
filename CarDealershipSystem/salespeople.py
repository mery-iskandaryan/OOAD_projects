import inventory
import cars


class Salesperson:
    total_inventory = []

    def __init__(self, name: str, commission_rate: float):
        self.name = name
        self._commission_rate = commission_rate
        self.inventory = inventory.Inventory()
        self.sales_history = ''
        Salesperson.total_inventory.append(self)

    @property
    def commission_rate(self) -> float:
        return self._commission_rate

    @commission_rate.setter
    def commission_rate(self, value: float) -> None:
        if not isinstance(value, float):
            raise TypeError("The rate should be a float.")
        self._commission_rate = value

    def add_car(self, car: 'Car') -> None:
        self.sales_history += f"Added: {car.make}, {car.model}: {car.price}\n"
        new_car = cars.Car(car.make, car.model, car.price + car.price*self.commission_rate/100)
        self.inventory.add_car(new_car)

    def remove_car(self, car: 'Car') -> None:
        self.sales_history += f"Removed: {car.make}, {car.model}: {car.price}\n"
        self.inventory.remove_car(car)
