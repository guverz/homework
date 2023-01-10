import time
def check_div_for_len():
    def check_div(x):
        num = x
        while(num != 0):
            p = num % 10
            num //= 10
            if (p == 0) or (x % p != 0):
                return False
        return True
    n, m = int(input("Введите n ")), int(input("Введите m "))
    start_time = time.time()
    for i in range(n, m + 1):
        if (check_div(i)):
            print(i)
    print("%s seconds" % (time.time() - start_time))

