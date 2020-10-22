import threading
import time


def p1(nm=""):
    while True:
        print("thread {} running....".format(nm))
        time.sleep(1)


def jumlah(a, b):
    t_awal = time.time()
    jml = 0
    for i in range(a, b):
        jml += i
    t_akhir = time.time()
    t_durasi = time.time() - t_awal
    # return i
    print("durasi {} dan t-akhir {}= {} \n".format(t_durasi, t_akhir, jml))


if __name__ == "__main__":
    # for i in range(10):
    #     threading.Thread(target=p1, args=("T{}".format(i),), daemon=True).start()
    #
    # while True:
    #     print("Program Utama")
    #     time.sleep(1)
    # jumlah(0, 1000001)
    # jumlah(10, 1000001)
    # jumlah(5, 1000001)

    threading.Thread(target=jumlah, args=(0, 5000000 + 1), daemon=True).start()
    threading.Thread(target=jumlah, args=(10, 5000000 + 1), daemon=True).start()
    threading.Thread(target=jumlah, args=(5, 5000000 + 1), daemon=True).start()

    while True:
        print("Main Program is running...")
        time.sleep(1)

    print("Finish")
