import time
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

check_season_2()
