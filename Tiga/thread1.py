import threading
import time


def p1(nm=""):
    while True:
        print("thread {} running....".format(nm))
        time.sleep(1)


if __name__ == "__main__":
    for i in range(10):
        threading.Thread(target=p1, args=("T{}".format(i),), daemon=True).start()

    while True:
        print("Program Utama")
        time.sleep(1)

    print("Finish")
