import time
def even_odd():
    n = int(input("Введите n "))
    start_time = time.time()
    sum_odd = 0
    sum_even = 0
    count_odd = 0
    count_even = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            sum_even += i
            count_even += 1
        else:
            sum_odd += i
            count_odd += 1
    print("Сумма четных ", sum_even)
    print("Кол-во четных ", count_even)
    print("Сумма нечетных ", sum_odd)
    print("Кол-во нечетных ", count_odd)
    print("%s seconds" % (time.time() - start_time))
