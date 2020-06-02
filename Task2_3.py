# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

season_list = ['зима', 'весна', 'лето', 'осень']
season_dict = {1: 'весна', 2: 'лето', 3: 'осень', 4: 'зима'}

number = int(input('Введите число от 1 до 12 (список): '));
if number in (1, 2, 12):
    print(season_list[0])
elif number > 2 and number <= 5:
    print(season_list[1])
elif number > 5 and number <= 8:
    print(season_list[2])
elif number > 8 and number <= 11:
    print(season_list[3])
else:
    print('Неверное число!')

number = int(input('Введите число от 1 до 12 (словарь): '));
if number > 2 and number <= 5:
    print(season_dict.get(1))
elif number > 5 and number <= 8:
    print(season_dict.get(2))
elif number > 8 and number <= 11:
    print(season_dict[3])
elif number in (1, 2, 12):
    print(season_dict[4])
else:
    print('Неверное число!')
