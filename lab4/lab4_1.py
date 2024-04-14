# Родительский класс Vehicle + main
class Vehicle:
    def __init__(self, model, price):
        self.model = model
        self.__price = price
        print("Vehicle __init__")

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Are you kidding?")

    def display_info(self):
        print("Model:", self.model, "Price:", self.get_price())

    def __del__(self):
        print("Vehicle destructor!")

