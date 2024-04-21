import queue
import threading
import time


def producer():
    print("Producer started")
    time.sleep(1)
    # Помещаем результат работы в очередь
    q.put("Result")
    print("Producer finished")


def consumer():
    # Блокируемся, пока в очереди не появится элемент
    print("Consumer started")
    result = q.get()
    print("Got result: ", result)
    print("Consumer finished")


q = queue.Queue()

thread1 = threading.Thread(target=producer)
thread2 = threading.Thread(target=consumer)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
