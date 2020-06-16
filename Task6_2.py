class Road:
    def __init__(self, length, width):
        try:
            self._lentgh, self._width = float(length), float(width)
            print(f"Необходимо {self.calc_mass()} тонн асфальта")
        except ValueError:
            print("Введите числовые значения!")

    def calc_mass(self):
        return round(self._lentgh * self._width * 25 * 5 * 0.001)


myRoad = Road(input("Длина(м): "), input("Ширина(м): "))
