import salespeople


class Customer:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self._contact_info = contact_info
        self.cars = []

    @property
    def contact_info(self):
        return self._contact_info

    def search_car(self, make: str, model: str) -> None:

        for salesman in salespeople.Salesperson.total_inventory:
            search_car = salesman.inventory.search_car(make, model)
            print(f"salesman: {salesman.name} - {search_car.make}, {search_car.model}, {search_car.price}")

    def purchase_car(self, make: str, model: str):
        car_dict = {}
        for salesman in salespeople.Salesperson.total_inventory:
            search_car = salesman.inventory.search_car(make, model)
            if search_car:
                car_dict[search_car.price] = search_car, salesman

        to_purchase = car_dict[min(car_dict)]
        self.cars.append(to_purchase[0])
        to_purchase[1].remove_car(to_purchase[0])


