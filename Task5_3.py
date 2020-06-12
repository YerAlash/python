try:
    with open("text_3.txt", "r", encoding="utf-8") as salary:
        salary_list = salary.read().split()
        salary_dict = {salary_list[i]: float(salary_list[i + 1])
                       for i in range(0, len(salary_list) - 1, 2)}
        print("Фамилии сотрудников, у которых оклад менее 20 тыс.: ", end="")
        print(', '.join(el for el in salary_dict.keys() if salary_dict.get(el) < 20000))
        print("Средняя величина доходов сотрудников: ", end="")
        print(sum(salary_dict.values()) / len(salary_dict))
except IOError:
    print("Ошибка ввода-вывода!")
