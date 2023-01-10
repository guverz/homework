import tkinter as tk
from tkinter import *
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
conversion_calc()
