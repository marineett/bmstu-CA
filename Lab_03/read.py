
def read_file():
    data = [[[None for _ in range(5)] for _ in range(5)] for _ in range(5)]
    with open("data.txt", "r") as f:
        i = 0
        while i < 5:
            j = 0
            while j < 5:
                line = list(f.readline().split())
                if line:
                    for k in range(5):
                        data[i][j][k] = int(line[k])
                    j += 1
            i += 1

    return data

def read_vals_pows():
    x = float(input("Введите значение x: "))
    y = float(input("Введите значение y: "))
    z = float(input("Введите значение z: "))

    nx = int(input("Введите степень для x: "))
    ny = int(input("Введите степень для y: "))
    nz = int(input("Введите степень для z: "))
    return x, y, z, nx, ny, nz