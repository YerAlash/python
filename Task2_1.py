#Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

first_list = [12, 3.14, 1 + 8j,                     # Number
              'Happiness',                          # String
              [108, 'Health'],                      # List
              (0, 1, False, True),                  # Tuple
              {None, 9, 'Aim'},                     # Set
              frozenset('Frozen Set'),              # Frozen Set
              {1: "Red", "key2": True, 3: None},    # Dictionary
              True,                                 # Boolean
              b"byte",                              # byte
              bytearray(b"byte array"),             # bytearray
              None,                                 # None
              ValueError                            # Exception
              ]

for ind, el in enumerate(first_list):
    print(ind + 1, el, {type(first_list[ind])})