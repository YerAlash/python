import os

file_name = 'text_1.txt'

try:
    os.remove(file_name)
except IOError:
    pass

print("Введите текст (для выхода пустая строка):")
while True:
    text = input()
    if not text:
        break
    else:
        with open(file_name, "a", encoding="utf-8") as file:
            file.write(text+"\n")
print(f"Текст записан в файле {file_name}")