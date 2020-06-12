from random import randrange
try:
    with open("text_5.txt", "w+", encoding="utf-8") as num_file:
        a_list = [str(randrange(-100, 100)) for _ in range(10)]
        print(" ".join(a_list), file=num_file)
        num_file.seek(0)
        content = num_file.read()
        print(f"Набор чисел в файле: {content}")
        print(f"Сумма чисел = {sum(map(int, content.split()))}")
except IOError:
    print("Ошибка ввода-вывода!")