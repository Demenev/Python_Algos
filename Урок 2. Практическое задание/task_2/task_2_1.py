"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
Для извлечения цифр числа используйте арифм. операции

Пример:
Введите натуральное число: 44
В числе 44 всего 2 цифр, из которых 2 чётных и 0 нечётных

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
NUMB = input("Введите натуральное число: ")
I = len(NUMB)
A = 0
B = 0
for i in range(I):
    if int(NUMB[i]) % 2 == 0:
        A +=1
    else:
        B +=1
print(f"В числе {NUMB} всего цифр - {I}, из них четных - {A}, нечетных - {B}")