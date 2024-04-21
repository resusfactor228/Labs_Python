import time
import requests


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

for i, url in enumerate(urls, start=1):
    get_content(url, f"content_{i}.txt")

print(f"EXEC TIME: {time.time() - time_}")
