import threading
import time

from joblib import Parallel, delayed # pip install joblib

def worker():
    print("Worker started")
    time.sleep(2)
    print("Worker finished")



# Stworzyć program, który równolegle pobiera i przetwarza dane z kilku stron internetowych.

if __name__ == "__main__":
    thread = threading.Thread(target=worker)
    # thread.daemon = True

    thread.start()

    print("Main program finished")