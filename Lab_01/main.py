if __name__ == "__main__":
    from funcs import *
    table = []
    func_y = []
    func_x = []
    F = []
    with open('08-02-2024-Исх_данные_лаб__1.txt') as f:
        f.readline()
        line = f.readline()
        while line:
            row = list(map(float, line.split()))
            table.append(row)
            line = f.readline()
    table.sort(key=lambda x: x[0])
    command = 10
    while command != 0:
        printInfo()
        try:
            command = int(input("Введите номер команды для ее выполнения: "))
        except Exception:
            command = 4
            print('Ошибка!\nНомер введенной команды некорректен. Попробуйте снова.')
        else:
            match command:
                case 0:
                    exit(0)
                case 1:
                    flag = False
                    while (flag != True):
                        try:
                            x = float(input("Введите x чтобы найти решение: "))
                            n = int(input("Введите степень полинома: "))
                        except Exception:
                            print('Ошибка!\nЧисло некорректно. Попробуйте снова.')
                        else:
                            if -1 < n < len(table):
                                flag = True
                            else:
                                print('Ошибка!\nЧисло n некорректно. Попробуйте снова.')
                    arr1 = getDots(n + 1, table, x)
                    if arr1 == None:
                        exit(0)
                    matrix1 = formMatrixNewton(arr1)
                    print('Таблица разделенных разностей для полинома Ньютона:')
                    printMatrix(matrix1)
                    print('Результат для полинома Ньютона:')
                    res = res_for_Newton(matrix1, x, n)
                    print(res)

                    arr2 = getDots((n + 1) // 3 + 1, table, x)
                    if arr2 == None:
                        exit(0)
                    matrix2 = formMatrixErmit(arr2, n + 1)
                    print('Таблица разделенных разностей для полинома Эрмита:')
                    printMatrix(matrix2)
                    print('Результат для полинома Эрмита:')
                    res_erm = res_for_Ermit(matrix2, x, n)
                    print(res_erm)
                    exit(0)
                case 2:
                    # Тут вместо х подставляем 0
                    try:
                        n = int(input("Введите степень полинома: "))
                    except Exception:
                        print('Ошибка!\nЧисло некорректно. Попробуйте снова.')
                    else:
                        if -1 < n < len(table):
                            flag = True
                        else:
                            print('Ошибка!\nЧисло n некорректно. Попробуйте снова.')
                    x = 0
                    for i in table:
                        i[0], i[1] = i[1], i[0]
                    arr1 = getDots(n + 1, table, x)
                    if arr1 == None:
                        exit(0)
                    matrix1 = formMatrixNewton(arr1)
                    print('Таблица разделенных разностей для полинома Ньютона:')
                    printMatrix(matrix1)
                    print('Результат для полинома Ньютона:')
                    res = res_for_Newton(matrix1, x, n)
                    print(res)

                    arr2 = getDots((n + 1) // 3 + 1, table, x)
                    if arr2 == None:
                        exit(0)
                    matrix2 = formMatrixErmit2(arr2, n + 1)
                    print('Таблица разделенных разностей для полинома Эрмита:')
                    printMatrix(matrix2)
                    print('Результат для полинома Эрмита:')
                    res_erm = res_for_Ermit(matrix2, x, n)
                    print(res_erm)
                    exit(0)
                case 3:
                    with open("y(x).txt") as file:
                        line = file.readline()
                        while line:
                            func_y.append(list(map(float, line.split())))
                            line = file.readline()
                    with open('x(y).txt') as file:
                        line = file.readline()
                        while line:
                            func_x.append(list(map(float, line.split())))
                            line = file.readline()
                    for i in func_x:
                        i[0], i[1] = i[1], i[0]
                    num = func_y[0][0]
                    while num < func_y[-1][0]:
                        arr = getDots_2(5, func_x, num)
                        matrix = formMatrixNewton(arr)
                        res = res_for_Newton(matrix, num, 4)
                        arr1 = getDots_2(5, func_y, num)
                        matrix1 = formMatrixNewton(arr1)
                        res_2 = res_for_Newton(matrix1, num, 4)
                        delta = abs(res_2 - res)
                        F.append([round(num, 3), round(delta, 3)])
                        num += 0.001
                    for i in F:
                        i[0], i[1] = i[1], i[0]
                    F.sort(key=lambda x: x[0])
                    arr = getDots(4, F, 0)
                    matrix = formMatrixNewton(arr)
                    x_res = res_for_Newton(matrix, 0, 3)
                    arr = getDots(4, func_y, x_res)
                    matrix = formMatrixNewton(arr)
                    y_res = res_for_Newton(matrix, x_res, 3)
                    print('X:', x_res, 'Y:', round(y_res, 3))
                    exit(0)