"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
def recursion(NUMB, A = 0, B = 0):
    if NUMB == 0:
        print(f"Количество четных и нечетных цифр в числе равно ({A}, {B})")
    else:
        N = NUMB % 10
        NUMB = NUMB // 10
        if N % 2 == 0:
            A +=1
            recursion(NUMB, A, B)
        else:
            B +=1
            recursion(NUMB, A, B)

recursion(122)