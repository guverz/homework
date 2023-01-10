import random as rnd
import time
def array_sum():
    start_time = time.time()
    n = rnd.randint(1, 50)
    end = [rnd.randint(1, 100) for _ in range(n)]
    print(end)
    print(sum(end))

    def sum_recursion(x, i=0):
        if i >= len(end):
            return 0
        return x[i] + sum_recursion(end, i + 1)

    start_time = time.time()
    print(sum_recursion(end))
    print("%s seconds" % (time.time() - start_time))
