# 4. Пользователь вводит целое положительное число. Найдите самую большую
# цифру в числе. Для решения используйте цикл while и арифметические операции.

number = int(input("Введите целое число: "))
max = 0
next_number = number
while True:
    current = next_number % 10
    if current > max:
        max = current
    next_number = next_number // 10
    if max == 9 or next_number == 0:
        break
print(f"Максимальная цифра в числе {number} : {max}")
