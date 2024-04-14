from lab4_1 import Vehicle


# Наследник Vehicle 2
class Bike(Vehicle):
    def __init__(self, model, price, wheel_size):
        Vehicle.__init__(self, model, price)
        self.__wheel_size = wheel_size
        print("Bike __init__")

    def get_wheel_size(self):
        return self.__wheel_size

    def set_wheel_size(self, wheel_size):
        if wheel_size > 0 and wheel_size.isdigit():
            self.__wheel_size = wheel_size
        else:
            print("Размер шины не может быть отрицательным или не числом")

    def __del__(self):
        print("Bike destructor!")

