import random as rnd
import time
def last_elem_vars():
    n = int(input('Введите n '))
    end = [rnd.randint(1, 100) for _ in range(n)]
    print(end)
    
    start_time1 = time.time()
    print("Используя индекс -1: ", end[-1])
    print("%s seconds" % (time.time() - start_time1))
   
    start_time2 = time.time()
    for i in range(0, len(end)):
        if i == (len(end) - 1):
            print("Через цикл : " + str(end[i]))
    print("%s seconds" % (time.time() - start_time2))
    
    start_time3 = time.time()
    end.reverse()
    print("Используя ревёрс через индекс : " + str(end[0]))
    print("%s seconds" % (time.time() - start_time3))
