from point_struct import Point

# Функция ищет индекс ближайшего к X значения в таблице
def get_index(table, x):
    diff = abs(table[0].x - x)
    index = 0

    for i in range(len(table)):
        if abs(table[i].x - x) < diff:
            diff = abs(table[i].x - x)
            index = i

    return index

# Функция ищет индекс ближайшего к Y значения в таблице
def get_y_index(table, y):
    diff = abs(table[0].y - y)
    index = 0

    for i in range(len(table)):
        if abs(table[i].y - y) < diff:
            diff = abs(table[i].y - y)
            index = i

    return index

# Функция считывает данные из файла и формирует таблицу значений
def read_table(filename):
    table = []
    file = open(filename)

    for line in file.readlines():
        row = list(map(float, line.split(" ")))
        table.append(Point(row[0], row[1], row[2]))

    file.close()
    return table
def print_table(table):
    print("┏" + "━━━━━━━" + ("┳" + "━━━━━━━━━━━━") * 3 + "┓")
    print("┃ {:^5s} ┃ {:^10s} ┃ {:^10s} ┃ {:^10s} ┃".format("№", "X", "Y", "Y'"))
    print("┣" + "━━━━━━━" + ("╋" + "━━━━━━━━━━━━") * 3 + "┫")

    for i in range(len(table)):
        print("┃ {:^5d} ┃ {:^10.3f} ┃ {:^10.3f} ┃ {:^10.3f} ┃".format(i,
                                                                      table[i].x,
                                                                      table[i].y,
                                                                      table[i].derivative))
    print("┗" + "━━━━━━━" + ("┻" + "━━━━━━━━━━━━") * 3 + "┛\n")

def print_diff_table(diff_table, n):
    length = len(diff_table)  # Получаем ширину таблицы

    # Выводим верхнюю границу таблицы
    print("┏" + "━━━━━━━━━━━━━━━━━━━━━" * length + "┓")
    print("┃ {:^18s} ┃ {:^18s}".format("X", "Y"), end=' ')  # Выводим заголовки столбцов X и Y

    # Выводим заголовки столбцов Y(i) для каждого i
    for k in range(2, length):
        print("┃ {:^18s}".format("Y" + "({0})".format(k - 1)), end=' ')
    print("┃")
    print("┣" + "━━━━━━━━━━━━━━━━━━━━━" * length + "┫")

    # Заполняем строки таблицы
    for i in range(n):  # Перебираем строки
        for j in range(length):  # Перебираем столбцы
            if j >= length - i:  # Если находимся в правой верхней части треугольника разностей, выводим пробел
                print("┃ {:^18s}".format(" "), end=' ')
            else:
                print("┃ {:^18.3f}".format(diff_table[j][i]), end=' ')  # Выводим значение разности с 3 знаками после запятой
        print("┃")

    # Выводим нижнюю границу таблицы
    print("┗" + "━━━━━━━━━━━━━━━━━━━━━" * length + "┛\n")
