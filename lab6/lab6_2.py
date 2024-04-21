import concurrent.futures
import time


def task(q, p):
    return 1 / (1 + abs(q - p))


time_ = time.time()
N = 500
P = [i for i in range(N)]
Q = [i for i in range(N)]

# Создаем пул потоков
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Запускаем несколько задач в отдельных потоках
    futures = [executor.submit(task, q, p) for q in Q for p in P]
    # Ждем, пока все задачи не завершатся, и получаем результаты
    results = [future.result() for future in futures]

print(results)
print("TIME OF EXEC: ", time.time() - time_)
