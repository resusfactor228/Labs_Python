import threading


def worker():
    print("Worker started")
    # time.sleep(2)
    # Дожидаемся, пока все потоки дойдут до барьера
    print("Waiting for barrier")
    barrier.wait()
    print("Worker finished")


# В данном примере не обеспечена другая синхронизация (помимо барьера) между запускаемыми потоками, поэтому
# может быть undefined behaviour при выводе сообщений Worker Finished
barrier = threading.Barrier(2)

thread1 = threading.Thread(target=worker)
thread2 = threading.Thread(target=worker)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
