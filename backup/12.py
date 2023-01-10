import random as rnd
import time
def array_reverse():
    start_time = time.time()
    n = rnd.randint(1, 50)
    end = [rnd.randint(1, 100) for _ in range(n)]
    print(end)
    end.reverse()
    print(end)
    print("%s seconds" % (time.time() - start_time))

