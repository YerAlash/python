# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(p1, p2, p3):
    try:
        my_list = [float(p1), float(p2), float(p3)]
        my_list.remove(min(my_list))
        return sum(my_list)
    except ValueError:
        print('Введен нечисловой символ!')

print("Сумма наибольших 2-х аргументов: "
      f"{my_func(input('1: '), input('2: '), input('3: '))}")
