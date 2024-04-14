import pytest
import pickle
from lab4.lab4_5 import Goods


class YesNoException(Exception):
    def __init__(self):
        super().__init__()


print("Построчно введите параметры товара:")
good = Goods(price=str(input()), discont=str(input()), height=str(input()), width=str(input()), depth=str(input()))

filename = "lab5_1.txt"

print("Записать в файл объект good? (Yes / No)")
try:
    answer = str(input())

    if answer == "Yes":
        with open(filename, "wb") as file:
            pickle.dump(good.get_price(), file)
            pickle.dump(good.get_discont(), file)
            pickle.dump(good.get_goods_size(), file)
    elif answer != "No":
        raise YesNoException

except IOError:
    print("Ошибка в названии файла!\t", IOError)
except YesNoException:
    print("Я же просил ввести Yes/No...")

good1 = Goods()

print("Восстановить из файла объект good? (Yes / No)")
try:
    answer = str(input())

    if answer == "Yes":
        with open(filename, "rb") as file:
            good1.set_price(pickle.load(file))
            good1.set_discont(pickle.load(file))
            good1_size = pickle.load(file)
            good1.set_goods_size(good1_size[0], good1_size[1], good1_size[2])
    elif answer != "No":
        raise YesNoException

except IOError:
    print("Ошибка в названии файла!\t", IOError)
except YesNoException:
    print("Я же просил ввести Yes/No...")
except TypeError:
    pass

print(good1.get_price(), good1.get_discont(), good1.get_goods_size())
