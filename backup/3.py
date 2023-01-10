import random as rnd
import time
def fifth_power_1():
    start_time = time.time()
    x = rnd.randint(0, 100)
    print('x:', x, x**5)
    print("%s seconds" % (time.time() - start_time))


def fifth_power_2():
    start_time = time.time()
    x = rnd.randint(0, 100)
    y = x*x*x*x*x
    print("x:", x, y)
    print("%s seconds" % (time.time() - start_time))


