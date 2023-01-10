import time
def pif_triples():
    n, m = (int(input("Введите n ")), int(input("Введите m ")))
    start_time = time.time()
    end = []
    for i in range(n, m + 1):
        for j in range(n, m + 1):
            for z in range(n, m + 1):
                if i ** 2 + j ** 2 == z ** 2:
                    end.append([i, j, z])
    [print(k) for k in end]
    print("%s seconds" % (time.time() - start_time))
pif_triples()