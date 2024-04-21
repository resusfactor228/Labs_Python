import time
import requests
import threading


def get_content(url_, filename):
    response = requests.get(url_)
    if response.status_code == 200:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(response.text)


time_ = time.time()

urls = [
    "https://miet.ru",
    "https://ya.ru",
    "https://google.com",
    "https://vk.com",
    "https://youtube.com",
    "https://ria.ru",
    "https://russian.rt.com",
    "https://www.songsterr.com",
    "https://www.google.com/maps",
    "https://ru.wikipedia.org"
]

# Создание и запуск потоков
threads = []
for i, url in enumerate(urls, start=1):
    thread = threading.Thread(target=get_content, args=(url, f"content_{i}.txt"))
    thread.start()
    threads.append(thread)

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()

print(f"EXEC TIME: {time.time() - time_}")
