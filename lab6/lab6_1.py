import threading
import time


# Определяем функцию, которую будем выполнять в потоке
def worker():
    # Блокируем семафор, ждем, пока он не станет доступен
    semaphore.acquire()
    print("Worker started")
    # Делаем какую-то работу
    time.sleep(1)
    print("Worker finished")
    # Освобождаем семафор
    semaphore.release()


# Создаем семафор с начальным значением 1
semaphore = threading.Semaphore(1)

# Создаем потоки, которые будут выполнять функцию worker
thread1 = threading.Thread(target=worker)
thread2 = threading.Thread(target=worker)
thread3 = threading.Thread(target=worker)
thread4 = threading.Thread(target=worker)

# Запускаем потоки
thread1.start()
thread2.start()
thread3.start()
thread4.start()

# Ждем, пока потоки не завершатся
thread1.join()
thread2.join()
thread3.join()
thread4.join()
