# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать
# вывод данных о пользователе одной строкой.


def f_usr_data(p_name, p_surname, p_dateofbirth, p_city, p_email, p_phone):
    return p_name, p_surname, p_dateofbirth, p_city, p_email, p_phone


print(f_usr_data(p_name=input('Имя:'), p_surname=input('Фамилия:'),
                 p_dateofbirth=input('Дата рождения:'), p_city=input('Город проживания:'),
                 p_email=input('Email:'), p_phone=input('Телефон:')))
