# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий
# склад. А также класс «Оргтехника», который будет базовым для
# классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры, общие
# для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.


class Warehouse:
    def __init__(self, type='OfficeEq'):
        self.type = type

class OfficeEquipment():
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

    def __str__(self):
        return f"Модель = {self.model}, год выпуска - {self.year}, " \
               f"цена - {self.price}"

class Scanner(OfficeEquipment):
    def __init__(self, model, year, price, sens_type):
        super().__init__(model, year, price)
        self.sens_type = sens_type

class Printer(OfficeEquipment):
    def __init__(self, model, year, price, is_color):
        super().__init__(model, year, price)
        self.is_color = is_color


class Xerox(OfficeEquipment):
    def __init__(self, model, year, price, is_3in1):
        super().__init__(model, year, price)
        self.is_3in1 = is_3in1


myPrinter = Printer("HP LaserJet 1020", 2020, 500, True)
print(myPrinter)

