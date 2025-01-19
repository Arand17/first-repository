"""Файл для запуска приложения"""

from models import Calculator
        

# Запуск приложения
if __name__ == "__main__":
    app = Calculator()
    app.run()