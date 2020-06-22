class Stationery:
    title = ''

    def draw(self):
        print("Start Rendering")


class Pen(Stationery):
    title = 'Pen'

    def draw(self):
        print(f"{self.title} is rendering")


class Pencil(Stationery):
    title = 'Pencil'

    def draw(self):
        print(f'Hello, I am a {self.title}')


class Handle(Stationery):
    title = 'Handle'

    def draw(self):
        print(f"{self.title} is drawing")


objStat = Stationery()
objStat.draw()
objPen = Pen()
objPen.draw()
objPencil = Pencil()
objPencil.draw()
objHandle = Handle()
objHandle.draw()
