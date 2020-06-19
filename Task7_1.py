# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
# класса (метод __init__()), который должен принимать данные (список списков)
# для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных
# в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
# привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения
# двух объектов класса Matrix (двух матриц). Результатом сложения должна быть
# новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
# первой строки первой матрицы складываем с первым элементом первой строки второй
# матрицы и т.д.

from random import randrange


def gen_dict():
    return [[randrange(-100, 101) for i in range(n)] for j in range(m)]


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        res = ''
        for j in range(m):
            for i in range(n):
                res = f"{res}{self.matrix[j][i]:3}{' ' * 3}"
            res = f"{res}\n\n"
        return res

    def __add__(self, other):
        list_ext = []
        for j in range(m):
            list_int = []
            for i in range(n):
                list_int.insert(i, self.matrix[j][i] + other.matrix[j][i]);
            list_ext.insert(j, list_int)
        return Matrix(list_ext)


try:
    print("Введите размерность матриц ниже (элементы будут заполнены "
          "автоматически случайными числами от -100 до 100):")
    n = int(input("  количество столбцов = "))
    m = int(input("  количество строк = "))
    matrix_1 = Matrix(gen_dict())
    matrix_2 = Matrix(gen_dict())
    print(f"1-матрица:\n{matrix_1}")
    print(f"2-матрица:\n{matrix_2}")
    print(f"Сложение:\n{matrix_1 + matrix_2}")
except ValueError:
    print("Введите целые числа!")
