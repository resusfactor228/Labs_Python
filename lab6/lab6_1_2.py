import threading
import time


def worker():
    with condition:
        print("Worker started")
        # Блокируем условие, ждем, пока не получим сигнал
        condition.wait()
    print("Worker finished")


condition = threading.Condition()

thread1 = threading.Thread(target=worker)
thread2 = threading.Thread(target=worker)

thread1.start()
thread2.start()

time.sleep(1)

with condition:
    print("Signal sent")
    condition.notify_all()

thread1.join()
thread2.join()
