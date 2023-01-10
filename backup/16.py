def sea_fight():
    a = [['0'] * 10 for _ in range(10)]
    ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    ships_end = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    print("Если хотите самостоятельно создать карту, введите 1. Если хотите создать карту из файла, введите 0")
    answer = int(input("Ответ: "))
    if answer == 1:
        print("Задайте координаты и положение (v - вертикально, h - горизонтально) корабля (Пример: '8 4 v', в таком случае, корабль появится на координатах с 8;4 по 8;7)")
        for j in range(len(ships)):
            print("Размер корабля: ", ships[j])
            y1, x1, d = map(str, input().split())
            x = int(x1) - 1
            y = int(y1) - 1        
            try:
                for i in range(ships_end.pop(0)):
                    if d == 'v':
                        a[x + i][y] = 1
                    elif d == 'h':
                        a[x][y + i] = 1
                    else:
                        print("Ошибка ввода положения корабля")
                        break
            except IndexError:
                print("Корабль не может быть установлен на данные координаты")
        for row in a:
            print(*row)
    elif answer == 0:
        name = input('Введите название файла, с расширением .txt: ')
        with open(name + '.txt') as f:
            for line in f:
                string = str(line)
                print(string, type(string))
                y1, x1, d = map(str, string.split())
                x = int(x1) - 1
                y = int(y1) - 1        
                try:
                    for i in range(ships_end.pop(0)):
                        if d == 'v':
                            a[x + i][y] = 1
                        elif d == 'h':
                            a[x][y + i] = 1
                        else:
                            print("Ошибка ввода положения корабля")
                            break
                except IndexError:
                    print("Корабль не может быть установлен на данные координаты")
            for row in a:
                print(*row)

sea_fight()

