try:
    with open("text_2.txt", "r", encoding="utf-8") as my_file:
        content = my_file.readlines()
        print(f"Количество строк в файле: {len(content)}")
        for ind, my_str in enumerate(content):
            print(f"{ind + 1} - строка: {len(my_str.split())} слов")
except IOError:
    print("Ошибка ввода-вывода!")