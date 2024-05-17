import newton
import hermit
import sys
from newton import get_diff_table, newton_calc, get_bordered_table
from hermit import *
from hermit import hermit_calc
from root import search_newton_root, search_hermit_root
from system import search_system_root
from table import *

filename = "./data/data.txt"
init_table = read_table(filename)
init_table = read_table(filename)
print("Изначальная таблица:")
print_table(init_table)

try:
    n = int(input("Введите степень n аппроксимирующих полиномов: "))
    x = float(input("Введите значение аргумента x, для которого выполняется интерполяция: "))
except ValueError:
    print("Ошибка: Введите корректные числовые значения.")
    sys.exit(1)


index = get_index(init_table, x)
table = get_bordered_table(init_table, index, n + 1)
print("Минимизированная таблица для расчётов:")
print_table(table)

diff_table = newton.get_diff_table(table, n)
print("Таблица разделённых разностей:")
print_diff_table(diff_table, n + 1)

newton_polynom = newton_calc(diff_table, n, x)
print("Полином Ньютона: {:.7f}\n\n".format(newton_polynom))

diff_table = hermit.get_diff_table(table)
print("Таблица разделённых разностей:")
print_diff_table(diff_table, 2 * len(table))

hermit_polynom = hermit_calc(diff_table, n, x)
print("Полином Эрмита: {:.7f}\n\n".format(hermit_polynom))


print("Вывод изначальной таблицы для поиска корней:")
print_table(init_table)

search_newton_root(init_table, n)
search_hermit_root(init_table)

print("\nРешение системы уравнений:\n")
print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
print("┃ Корни системы следующие:                ┃")
print("┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃")
search_system_root(n)
print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n")