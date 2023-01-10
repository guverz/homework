from math import sqrt
import time
def check_fibon_num():
    a = int(input("Введите число для проверки "))
    start_time = time.time()
    try:
        if 250 >= a >= 0:
            if (sqrt(5 * (a ** 2) + 4) % 1 == 0) or (sqrt(5 * (a ** 2) - 4) % 1 == 0):
                print("Это число Фибоначчи")
                print("--- %s seconds ---" % (time.time() - start_time))
            else:
                print("Это не число Фибоначчи")
                print("--- %s seconds ---" % (time.time() - start_time))
        else:
            print("Число вне диапазона")
            print("--- %s seconds ---" % (time.time() - start_time))
    except ValueError:
        print("Введено не целое число")
        print("--- %s seconds ---" % (time.time() - start_time))

check_fibon_num()