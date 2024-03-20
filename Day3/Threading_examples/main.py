import threading
import time
import requests

from joblib import Parallel, delayed # pip install joblib

def worker():
    print("Worker started")
    time.sleep(2)
    print("Worker finished")


def calculate_sum(data: list[int], start: int, end: int, result: list[int]):
    partial_sum = sum(data[start:end])
    result.append(partial_sum)


def main_threading():
    data = list(range(1000000))
    num_threads = 4
    chunk_size = len(data) // num_threads

    result = []
    threads = []
    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size if i < num_threads - 1 else len(data)
        thread = threading.Thread(target=calculate_sum, args=(data, start, end, result))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    total_sum = sum(result)
    print("Total sum:", total_sum)


from joblib import Parallel, delayed  # https://joblib.readthedocs.io/en/stable/


# def calculate_sum2(data_chunk):
#     return sum(data_chunk)
#
# def main_joblib():
#     data = list(range(1000000))
#     num_jobs = 4
#     chunk_size = len(data) // num_jobs
#
#     data_chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
#     results = Parallel(n_jobs=num_jobs)(delayed(calculate_sum2)(chunk) for chunk in data_chunks)
#
#     total_sum = sum(results)
#     print("Total sum:", total_sum)


# Stworzyć program, który równolegle pobiera i przetwarza dane z kilku stron internetowych.
def fetch_and_count_words(url):
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        words_count = len(content.split())
        print(f"Words count from {url}: {words_count}")


def threading_urls():
    urls = [
        "https://example.com",
        "https://www.python.org",
        "https://www.wikipedia.org"
    ]
    threads = []
    for url in urls:
        thread = threading.Thread(target=fetch_and_count_words, args=(url,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    # thread = threading.Thread(target=worker)
    # thread.daemon = True
    #
    # thread.start()
    #
    # print("Main program finished")

    #main_threading()

    #main_joblib()

    threading_urls()