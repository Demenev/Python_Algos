"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
from random import random

A = int(random() * 100)
print(A)
B = 0
for i in range(10):
    B = int(input("Введите число от 0 до 100 "))
    if B == A:
        print("Вы угадали")
        break
    else:
        print("Вы не угадали, загаданное число больше" if A > B else "Загаданное число меньше")
print(f"Количество попыток закончилось. Загаданное число {A}")