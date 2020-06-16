from colorama import Fore
from time import sleep


class TrafficLight:
    __color = ''

    def running(self):
        color_dict = {'RED': (Fore.RED, 5), 'GREEN': (Fore.GREEN, 5),
                      'YELLOW': (Fore.YELLOW, 2)}
        color_tuple = ('RED', 'YELLOW', 'GREEN', 'YELLOW')
        while True:
            for el in color_tuple:
                self.__color = el
                print(color_dict[el][0] + self.__color)
                sleep(color_dict[el][1])


light = TrafficLight()
light.running()
