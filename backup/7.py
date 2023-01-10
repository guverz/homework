import time
def find_divide():
    n = int(input("Введите число от 1 до 249 включительно"))
    start_time = time.time()    
    k = 0
    if 249 >= n >= 1:
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                if i % j == 0:
                    k += 1
            print(i, k)
            k = 0
    else:
        print("Число вне диапазона") 
    print("%s seconds" % (time.time() - start_time))
