def newton(data, x, y, z, nx, ny, nz):
    zs = []
    for i in range(5):
        ys = []
        for j in range(5):
            xs = []
            for k in range(5):
                xs.append([k, data[i][j][k]])
            ys.append([j, NewtonMethod(xs, x, nx)])
        zs.append([i, NewtonMethod(ys, y, ny)])
    return NewtonMethod(zs, z, nz)

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
            return table[i][1]
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

def formMatrixNewton(arrOfDots):
    matrix = []
    ind = 2
    for i in arrOfDots:
        matrix.append([i[0], i[1]])
    for i in range(len(arrOfDots)):
        matrix = formColumnNewton(matrix, ind, len(arrOfDots))
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

# def printMatrix(matrix):
#     str = (len(matrix[-1]) * 11 + 1) * '-'
#     print(str, end='')
#     for i in range(len(matrix)):
#         print("\n|", end="")
#         for j in range(len(matrix[i])):
#             a = round(matrix[i][j], 3)
#             print(f"{a:>10}|", end="")
#     print()
#     print(str)

def NewtonMethod(table, val, pow):
    arrOfDots = getDots(pow + 1, table, val)
    matrix = formMatrixNewton(arrOfDots)
    res = res_for_Newton(matrix, val, pow)
    return res


