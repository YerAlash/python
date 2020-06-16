# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо
# предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении
# числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие,
# при котором повторение элементов списка будет прекращено.

from sys import argv
from itertools import count
from itertools import cycle
from random import randint    

try:
    p_scr_name, p_number = argv
    try:
        p_number = int(p_number)
        if p_number == 0:           # для вывода варианта б)
            lights = ['Green', 'Yellow', 'Red']
            temp_i = len(lights)
            repeat_count = randint(temp_i, temp_i ** 3)
            an_iter = cycle(lights)
            temp_i = 0
            while temp_i < repeat_count:
                print(next(an_iter))
                temp_i += 1
        else:
            repeat_count = randint(3, 10)
            for i in count(p_number):
                if i >= p_number + repeat_count:
                    break
                print(i)
        print(f"Количество элементов для вывода (случайное): {repeat_count}")
    except ValueError:
        print('Введите целое число!')
except ValueError:
    print('Неверное количество параметров!')
    print('Параметры: имя скрипта, целое число (0 - вариант b)')
