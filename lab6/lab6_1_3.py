import threading


def worker():
    print("Worker started")
    # Ждем, пока событие не наступит
    event.wait()
    print("Worker finished")


event = threading.Event()

thread1 = threading.Thread(target=worker)
thread2 = threading.Thread(target=worker)

thread1.start()
thread2.start()

event.set()

thread1.join()
thread2.join()
