import time
import random as rnd
from math import sqrt
import tkinter as tk
from tkinter import *

def exchange():
    a, b, c = [input('Введите a '), input('Введите b '), input('Введите c ')]
    a, b, c = b, c, a
    print(a, b, c)

def num_check():
    while True:
        try:
            n = int(input("Вставьте n "))            
            end = []            
            for _ in range(n):
                end.append(int(input("Вставьте число ")))
            start_time = time.time()            
            for j in end:
                mark = True
                if isinstance(j, int):
                    mark = True
                else:
                    mark = False
            if mark == True:
                print(sum(end))
                print("%s seconds" % (time.time() - start_time))
                break
            else:
                print('Повторите снова')
        except ValueError:
            print("Введено не число")

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


def check_fibon_num():
    a = int(input("Введите число для проверки "))
    start_time = time.time()
    try:
        if 250 >= a >= 0:
            if (sqrt(5 * (a ** 2) + 4) % 1 == 0) or (sqrt(5 * (a ** 2) - 4) % 1 == 0):
                print("Это число Фибоначчи")
                print("--- %s seconds ---" % (time.time() - start_time))
            else:
                print("Это не число Фибоначчи")
                print("--- %s seconds ---" % (time.time() - start_time))
        else:
            print("Число вне диапазона")
            print("--- %s seconds ---" % (time.time() - start_time))
    except ValueError:
        print("Введено не целое число")
        print("--- %s seconds ---" % (time.time() - start_time))

def check_season_1():
    a = int(input("Введите число месяца (1 - 12) "))
    start_time = time.time()
    if a == 12 or a == 1 or a == 2:
        print("Зима") 
    if a == 3 or a == 4 or a == 5:
        print("Весна")
    if a == 6 or a == 7 or a == 8:
        print("Лето")
    if a == 9 or a == 10 or a == 11:
        print("Осень")
    else:
        print("Введено число не месяца")
    print("%s seconds" % (time.time() - start_time))

def check_season_2():
    a = int(input('Введите число месяца (1 - 12) '))    
    start_time = time.time()
    seasons = {'Зима': (1, 2, 12),
             'Весна': (3, 4, 5),
             'Лето': (6, 7, 8),
             'Осень': (9, 10, 11)}
    for key in seasons.keys():
        if a in seasons[key]:
            print(key)
            print("%s seconds" % (time.time() - start_time))

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
    print("%s seconds" % (time.time() - start_time))

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

def array_reverse():
    start_time = time.time()
    n = rnd.randint(1, 50)
    end = [rnd.randint(1, 100) for _ in range(n)]
    print(end)
    end.reverse()
    print(end)
    print("%s seconds" % (time.time() - start_time))

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

def conversion_calc():
    screen = tk.Tk()
    screen.title("Conversion")
    screen.geometry("640x480")
    def conversion_rub_dollar():
        a = ruble.get()
        b = 0.014225
        try:
            a = float(a)
            result1.delete(0, END)
            result1.insert(0, a * b)
        except ValueError:
            result1.delete(0, END)
            result1.insert(0, "Извините, в переменных не числа")
    
    def conversion_dollar_rub():
        d = dollar.get()
        c = 70.3
        try:
            d = float(d)
            result2.delete(0, END)
            result2.insert(0, d * c)
        except ValueError:
            result2.delete(0, END)
            result2.insert(0, "Извините, в переменных не числа")
    
    tk.Label(screen, text="Кол-во рублей").pack(anchor = "w")
    ruble = tk.Entry(screen, font="Arial 16", bg="#6D87D6")
    ruble.insert(0, 0)
    ruble.pack(anchor = "w")

    tk.Label(screen, text="Курс 0.014225").pack(anchor = "w")
    
    tk.Label(screen, text="Итого долларов").pack(anchor = "w")
    result1 = tk.Entry(screen, font="Arial 16", bg ="#FFB673")
    result1.pack(anchor = "w")
    
    tk.Button(screen, text="Получить USD", command=conversion_rub_dollar).pack(anchor = "w")
    
    tk.Label(screen, text="Кол-во долларов").pack(anchor = "e")
    dollar = tk.Entry(screen, font="Arial 16", bg="#FFB673")
    dollar.insert(0, 0)
    dollar.pack(anchor = "e")

    tk.Label(screen, text="Курс 70.3").pack(anchor = "e")
    
    tk.Label(screen, text="Итого рублей").pack(anchor = "e")
    result2 = tk.Entry(screen, font="Arial 16", bg ="#6D87D6")
    result2.pack(anchor = "e")
    
    tk.Button(screen, text="Получить RUB", command=conversion_dollar_rub).pack(anchor = "e")
    screen.mainloop

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

