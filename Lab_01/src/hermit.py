import numpy

EPS = 1e-8

# Функция для проверки приближенного равенства двух чисел с плавающей точкой
def equal(a, b):
    return abs(a - b) < EPS

# Функция для вычисления таблицы разделеaнных разностей
def get_diff_table(table, mode=0):
    diff_table = []
    row_shift = 2

    if not mode:
        for point in table:
            diff_table.append([point.x, point.y])
            diff_table.append([point.x, point.y])

        diff_table = list([list(row) for row in numpy.transpose(diff_table)])

        yd_row = []
        x_row = diff_table[0]
        y_row = diff_table[1]
        ind = 2

        for point in table:
            yd_row.append(point.derivative)
            if ind < len(x_row):
                if y_row[ind - 1] is None or y_row[ind] is None or x_row[ind - 1] is None or x_row[ind] is None:
                    yd_row.append(None)
                else:
                    yd_row.append((y_row[ind - 1] - y_row[ind]) / (x_row[ind - 1] - x_row[ind]))
                ind += 2
        diff_table.append(yd_row)

    if mode:
        diff_table = table

    x_row = diff_table[0]

    for i in range(row_shift, len(x_row)):
        diff_table.append([])
        cur_y_row = diff_table[len(diff_table) - 2]
        for j in range(0, len(x_row) - i):
            if equal(x_row[j], x_row[j + i]):
                cur = yd_row[j]
            else:
                if cur_y_row[j] is None or cur_y_row[j + 1] is None or x_row[j] is None or x_row[j + i] is None:
                    cur = None
                else:
                    cur = (cur_y_row[j] - cur_y_row[j + 1]) / (x_row[j] - x_row[j + i])
            diff_table[i + row_shift - 1].append(cur)

    return diff_table

# Функция для вычисления значения полинома Эрмита в точке z
def hermit_calc(diff_table, n, z):
    row_shift = 2  # Смещение строк в таблице
    res = diff_table[1][0]  # Начальное значение полинома (верхняя строка в столбце Y)
    left_part = 1  # Начальное значение левой части выражения

    for i in range(n):
        left_part *= (z - diff_table[0][i])  # Вычисляем (Z - Y(Z))
        if diff_table[i + row_shift][0] is not None:  # Проверяем, не является ли значение None
            res += left_part * diff_table[i + row_shift][0] # Вычисляем полином, учитывая разделенные разности

    return res  # Возвращаем значение полинома
