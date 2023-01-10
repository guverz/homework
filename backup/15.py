def mult_table():
    n, m = int(input("Введите n")), int(input("Введите m "))
    try:
        if 20 >= n >= 5 and 20 >= m >= 5:
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    print(i * j, end = " ")
                print("")
        else:
            print("Число не входит в диапазон")
    except ValueError:
        print("Введены не целые числа")
mult_table()