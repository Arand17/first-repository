"""Файл с описанием главного класса приложения"""

import tkinter as tk
from tkinter import font
from keyboard import add_hotkey
from sympy import sympify, SympifyError


# Главный класс
class Calculator:
    def __init__(self):
        # Создание окна
        self.root = tk.Tk()
        self.root.title("Калькулятор")
        self.root.geometry("400x420")
        self.root.configure(bg='white')
        
        # Шрифт
        self.font = "Times"
        self.custom_font = font.Font(family=self.font, size=100, weight="bold")
        
        # Экран (ввод и вывод) для отображения результата
        self.display = tk.Entry(self.root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
        self.display.pack(pady=10)  # Отступы сверху и снизу

        # Фрейм для кнопок
        button_frame = tk.Frame(self.root)
        button_frame.pack(side=tk.BOTTOM)
        
        # Bind-им кнопку enter
        add_hotkey('enter', self.output)
        
        
        # Создание всех кнопок
        buttons = [
            '1', '2', '3', '/', '!',
            '4', '5', '6', '*', '^',
            '7', '8', '9', '-', '%',
            'C', '0', '=', '+', '.'
        ]
        
        rows = 4
        columns = 5

        for i in range(rows):  # 4 строки
            for j in range(columns):  # 5 столбцов
                button_text = buttons[i * columns + j]
                action = lambda x=button_text: self.on_button_click(x)
                tk.Button(button_frame, text=button_text, width=5, height=2, font=('Arial', 18), command=action).grid(row=i, column=j)
                

    # Функция, вызов которой происходит при нажатии на кнопку
    def on_button_click(self, char):
        if self.display.get() == "Ошибка":
            self.display.delete(0, tk.END)
            
        if char == 'C': self.display.delete(0, tk.END)  # Очистка экрана
        elif char == '=': self.output()
        else: self.display.insert(tk.END, char)
    
    # Функция для расчета и вывода результата
    def output(self):
        try:
            result = sympify(self.display.get())  # Вычисление выражения и перевод в строку
            self.display.delete(0, tk.END)
            if type(result) is float: self.display.insert(tk.END, f"{result:.6f}")
            else: self.display.insert(tk.END, f"{result}")
        except SympifyError:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Ошибка")
    
    # Функция запуска и удерживания окна
    def run(self):
        self.root.mainloop()
        