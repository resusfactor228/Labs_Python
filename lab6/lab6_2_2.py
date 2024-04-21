import time


def task(q, p):
    return 1 / (1 + abs(q - p))


time_ = time.time()
N = 500
P = [i for i in range(N)]
Q = [i for i in range(N)]

results = [task(q, p) for q in Q for p in P]

print(results)
print("TIME OF EXEC: ", time.time() - time_)

# Скорость выполнения выше у модуля без concurrent.futures (~0.2 сек < ~5 сек) ввиду отсутствия больших накладных расходов
# на создание новых потоков для таких немассивных вычислительных операций как 1 / (1 + abs(q - p))
