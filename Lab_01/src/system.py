import numpy
import newton
import hermit
from newton import *
from hermit import *
from point_struct import Point
from root import search_newton_root, search_hermit_root
from table import get_index, print_table, get_y_index

# Функция формирует систему уравнений из файлов и возвращает таблицу значений
def get_system_table():
    table = []
    file = open("./data/system1.txt")

    for line in file.readlines():
        row = list(map(float, line.split(" ")))
        table.append([row[0], row[1], None])

    file = open("./data/system2.txt")

    for line in file.readlines():
        row = list(map(float, line.split(" ")))
        table.append([row[0], None, row[1]])

    table.sort()

    file.close()
    return table

# Функция дополняет таблицу значений, вычисляя отсутствующие значения по заданным точкам
def complement_table(table):
    n = 3
    # таблицы разностей по данным 0 и (1 или 2) строк
    table1 = []
    table2 = []
    for i in range(len(table)):
        if table[i][1] is not None:
            table1.append([table[i][0], table[i][1]])
        else:
            table2.append([table[i][0], table[i][2]])

    diff_table1 = newton.get_diff_table(table1, n, 1)
    diff_table2 = newton.get_diff_table(table2, n, 1)

    for i in range(len(table)):
        if table[i][2] is None:
            table[i][2] = newton_calc(diff_table2, n, table[i][0])
        if table[i][1] is None:
            table[i][1] = newton_calc(diff_table1, n, table[i][0])

    return table

# Функция вычитает значения y2 из y1 для каждой точки таблицы
def subtract_table(table):
    new_table = []

    for i in range(len(table)):
        new_table.append(Point(table[i][0], table[i][1] - table[i][2], None))

    return new_table

# Функция ищет корни системы уравнений
def search_system_root(n):

    table = get_system_table() # Получаем таблицу значений системы
    table = complement_table(table) # Дополняем таблицу
    table = subtract_table(table) # Вычитаем значения
    index = get_y_index(table, 0) # Получаем индекс начала таблицы по y

    table = get_bordered_table(table, index, n + 1) # Получаем ограниченную таблицу
    search_newton_root(table, n) # Ищем корни методом Ньютона
    search_hermit_root(table)
