def exchange():
    a, b, c = [input('Введите a '), input('Введите b '), input('Введите c ')]
    a, b, c = b, c, a
    print(a, b, c)
