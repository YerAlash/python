# 7. Реализовать проект «Операции с комплексными числами». Создайте класс
# «Комплексное число», реализуйте перегрузку методов сложения и умножения
# комплексных чисел. Проверьте работу проекта, создав экземпляры класса
# (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNum:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return f"{self.x}{'+' if self.y >= 0 else ''}{self.y}i"

    def __add__(self, other):
        return ComplexNum(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return ComplexNum(self.x * other.x - self.y * other.y,
                          self.x * other.y + other.x * self.y)


try:
    real_part = "Enter the real part: "
    img_part = "Enter the imaginary part: "
    num1 = ComplexNum(input(real_part), input(img_part))
    print(num1)
    num2 = ComplexNum(input(real_part), input(img_part))
    print(num2)
    print(f"Adding = {num1 + num2}")
    print(f"Multiplication = {num1 * num2}")
except ValueError:
    print("Enter integer number!")
