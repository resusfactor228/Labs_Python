class Goods:

    def __init__(self, **kwargs):
        try:
            self.__price = float(kwargs["price"])
            self.__discont = float(kwargs["discont"])
            self.__height = float(kwargs["height"])
            self.__width = float(kwargs["width"])
            self.__depth = float(kwargs["depth"])
        except KeyError:
            pass
        except ValueError:
            print("Одно из значений было передано не в виде числа, преобразовано в None!")

    def get_discont(self):
        try:
            return self.__discont
        except AttributeError:
            pass

    def set_discont(self, discont):
        try:
            if 0 <= discont <= 100:
                self.__discont = discont
            else:
                print("Скидка не может быть отрицательной")
        except ValueError:
            print("Скидка должна быть числом!", ValueError)

    def get_price(self):
        try:
            return self.__price
        except AttributeError:
            pass

    def set_price(self, price):
        try:
            if price >= 0.01:
                self.__price = price
            else:
                print("Цена должна быть не меньше 0.01")
        except ValueError:
            print("Введите цену как число!", ValueError)

    def get_goods_size(self):
        try:
            return self.__height, self.__width, self.__depth
        except AttributeError:
            pass

    def set_goods_size(self, height, width, depth):
        try:
            if height <= 0 or width <= 0 or depth <= 0:
                print("Длина, ширина или глубина товара должны быть положительными")
            else:
                self.__height = height
                self.__width = width
                self.__depth = depth
        except ValueError:
            print("Введите параметры как числа!", ValueError)

    def get_price_with_discont(self):
        try:
            return float(self.__price) - float(self.__price) * float(self.__discont) / 100
        except ValueError:
            print("Все параметры должны быть числами!")

    def how_much_can_fit(self, height, width, depth):
        try:
            if height <= 0 or width <= 0 or depth <= 0:
                print("Длина, ширина или глубина коробки должны быть положительными")
            else:
                if height < self.__height or width < self.__width or depth < self.__depth:
                    print("Длина, ширина или глубина коробки не могут быть меньше товара")
                else:
                    return height // self.__height * width // self.__width * depth // self.__depth
        except ValueError:
            print("Все параметры должны быть числами!")

    # Оператор принимает на вход цену и скидку, их сумма будет вычислена как сумма со скидкой
    def __add__(self, other):
        try:
            return float(self.__price) - float(self.__price) * float(other) / 100
        except ValueError:
            print("Все параметры должны быть числами!")

# Раскомментить все снизу для проверки работоспособности методов класса
# good = Goods(discont="25", price="1234", height="10", width="20", depth="30")
# print("Цена со скидкой", good.get_price_with_discont())
# print("В коробке может поместиться", good.how_much_can_fit(30, 20, 30), "штуки товара")
# print("Цена со скидкой", good + 50)
