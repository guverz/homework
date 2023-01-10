import time
def perfect_num():
    n = int(input("Введите N < 5 "))
    count = 0
    sum = 0
    start_time = time.time()
    if n < 5:    
        for i in range(1, 9000):
            for j in range(1, i):
                if i % j == 0:
                    sum += j
            if sum == i:
                count += 1
                if count <= n:
                    print(i)
                sum = 0 
            else:
                sum = 0
    else:
        print("Число вне диапазона")
    print("--- %s seconds ---" % (time.time() - start_time))
t10()
