# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать
# дату в виде строки формата «день-месяц-год». В рамках класса реализовать
# два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Date:

    def __init__(self, date):
        self.date = date

    @property
    def check(self):
        return Date.to_int_list(self.date)

    @classmethod
    def to_int_list(cls, par_date=None):
        try:
            if par_date is None:
                par_date = Date(input(enter_text)).date
            res_list = list(map(int, par_date.split('-')))
            if len(res_list) != 3:
                raise ValueError
            return Date.validate(res_list)
        except ValueError:
            return "Неверный формат даты!"

    @staticmethod
    def validate(date_list):
        if not date_list[2] > 0:
            return "Год должен быть больше нуля!"
        if not 1 <= date_list[1] <= 12:
            return "Месяц должен быть в диапазоне 1:12!"
        if date_list[0] > 31:
            return "Число (день) должно быть в диапазоне 1:31!"
        # Дополнительные проверки
        # Февраль
        if date_list[1] == 2:
            if date_list[2] % 4 == 0 and date_list[0] > 29:
                return "В феврале 29 дней!"
            elif date_list[0] > 28:
                return "В феврале 28 дней!"

        if (date_list[1] <= 7 and date_list[1] % 2 == 0 or
            date_list[1] >= 8 and date_list[2] % 2 != 0) and date_list[0] > 30:
            return "В этом месяце 30 дней!"
        else:
            return "Введена корректная дата"


enter_text = "Введите дату в формате «день-месяц-год»: "
print(Date.to_int_list())
myDate = Date(input(enter_text))
print(myDate.check)
