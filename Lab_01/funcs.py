def getDots(n, table, x):
    i = 0
    if x > table[-1][0]:
        beg = len(table) - 1 - n
        end = len(table)
    elif x < table[0][0]:
        beg = 0
        end = n
    else:
        while x > table[i][0]:
            i += 1
        if x == table[i][0]:
            print("Ответ: ", table[i][1])
            return None
        else:
            beg = i
            end = i
            cnt = 0
            while cnt < n:
                if beg > 0:
                    beg -= 1
                    cnt += 1
                if end < (len(table)) and cnt < n:
                    end += 1
                    cnt += 1
    arrOfDots = table[beg:end]
    return arrOfDots

def formColumnNewton(matrix, ind, n):
    for i in range(ind - 1, n):
        matrix[i].append((matrix[i - 1][ind - 1] - matrix[i][ind - 1]) / (matrix[i - ind + 1][0] - matrix[i][0]))
    return matrix

def formColumnErmit(matrix, ind, n, arr):
    for i in range(ind - 1, n):
        a = matrix[i - 1][ind - 1] - matrix[i][ind - 1]
        b = matrix[i - ind + 1][0] - matrix[i][0]
        if a == 0 or b == 0:
            if ind == 2:
                matrix[i].append(arr[i - ind + 1][2])
            elif ind == 3:
                matrix[i].append(1 / 2 * arr[i - ind + 1][3])
        else:
            matrix[i].append(a / b)
    return matrix


def formMatrixNewton(arrOfDots):
    matrix = []
    ind = 2
    for i in arrOfDots:
        matrix.append([i[0], i[1]])
    for i in range(len(arrOfDots)):
        matrix = formColumnNewton(matrix, ind, len(arrOfDots))
        ind += 1
    return matrix

def formMatrixErmit(arrOfDots, n):
    matrix = []
    ind = 2
    i = 0
    cnt = 0
    amount = 0
    arr = []
    while amount < n:
        arr.append([arrOfDots[i][0], arrOfDots[i][1], arrOfDots[i][2], arrOfDots[i][3]])
        matrix.append([arrOfDots[i][0], arrOfDots[i][1]])
        cnt += 1
        if cnt == 3:
            cnt = 0
            i += 1
        amount += 1
    for i in range(n):
        matrix = formColumnErmit(matrix, ind, n, arr)
        ind += 1
    return matrix


def formMatrixErmit2(arrOfDots, n):
    matrix = []
    ind = 2
    i = 0
    cnt = 0
    amount = 0
    arr = []
    while amount < n:
        arr.append([arrOfDots[i][0], arrOfDots[i][1], 1 / arrOfDots[i][2], arrOfDots[i][3] / (arrOfDots[i][2] ** 3)])
        matrix.append([arrOfDots[i][0], arrOfDots[i][1]])
        cnt += 1
        if cnt == 3:
            cnt = 0
            i += 1
        amount += 1
    for i in range(n):
        matrix = formColumnErmit(matrix, ind, n, arr)
        ind += 1
    return matrix

def res_for_Newton(matrix, x, n):
    res = matrix[0][1]
    for i in range(n):
        mul = matrix[i + 1][i + 2]
        for j in range(i + 1):
            mul *= x - matrix[j][0]
        res += mul
    return res

def res_for_Ermit(matrix, x, n):
    res = matrix[0][1]
    for i in range(n):
        mul = matrix[i + 1][i + 2]
        for j in range(i + 1):
            mul *= x - matrix[j][0]
        res += mul
    return res

def printMatrix(matrix):
    str = (len(matrix[-1]) * 11 + 1) * '-'
    print(str, end='')
    for i in range(len(matrix)):
        print("\n|", end="")
        for j in range(len(matrix[i])):
            a = round(matrix[i][j], 3)
            print(f"{a:>10}|", end="")
    print()
    print(str)

def printInfo():
        print("У программы есть команды, чтобы их выполнить введите номер команды.\n"
              "1. Получить таблицу значений степеней полиномов Ньютона и Эрмита\n"
              "при фиксированном x. Сравнить результаты для полинома Ньютона и Эрмита.\n"
              "2. Найти корень данной табличной функции с помощью обратной интерполяции\n"
              "обоими полиномами.\n"
              "3. Решить систему нелинейных уравнений, основываясь на идее обратной\n"
              "интерполяции.\n"
              "0. Завершить выполнение программы.\n")


def getDots_2(n, table, x):
    i = 0
    if x > table[-1][0]:
        beg = len(table) - 1 - n
        end = len(table)
    elif x < table[0][0]:
        beg = 0
        end = n
    else:
        while x > table[i][0]:
            i += 1
        beg = i
        end = i
        cnt = 0
        while cnt < n:
            if beg > 0:
                beg -= 1
                cnt += 1
            if end < (len(table)) and cnt < n:
                end += 1
                cnt += 1
    arrOfDots = table[beg:end]
    return arrOfDots