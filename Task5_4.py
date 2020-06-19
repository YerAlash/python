import os

rus_words = ('Один', 'Два', 'Три', 'Четыре')
lat_words = ('One', 'Two', 'Three', 'Four')
i = 0
file_name = "text_4_rus.txt"

try:
    os.remove(file_name)
except IOError:
    pass
try:
    with open("text_4.txt", "r", encoding="utf-8") as translate:
        for line in translate:
            line = line.replace(lat_words[i], rus_words[i])
            with open(file_name, "a", encoding="utf-8") as cyril:
                cyril.write(line)
            i += 1
    print(f'Исходный текст переведен и записан в файле {file_name}')
except IOError:
    print("Ошибка ввода-вывода!")
