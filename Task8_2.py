class MyZeroErr(Exception):
    def __init__(self, text):
        self.text = text


try:
    div_list = list(map(float, input(
        "Введите 2 числа, разделенные пробелом: ").split()))
    if len(div_list) != 2:
        raise ValueError
    if div_list[1] == 0:
        raise MyZeroErr("Деление на нуль!")
except ValueError:
    print("Введены нечисловые значения, либо более 2-х чисел!")
except MyZeroErr as err:
    print(err)
else:
    print(f"Частное введенных чисел = {round(div_list[0] / div_list[1], 5)}")
