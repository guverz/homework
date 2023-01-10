import time
def num_check():
#    start_time_for_error = time.time()
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
#            print("%s second" % (time.time() - start_time_for_error))

num_check()
