from read import read_file, read_vals_pows
from newton import newton
from spline import spline
from mixed import mixed

data = read_file()
x, y, z, nx, ny, nz = read_vals_pows()

print('-' * 50)
string = str(round(newton(data, x, y, z, nx, ny, nz), 4))
print('|', f"{'Ньютон' : ^30}", '|', f"{string : ^13}", '|')
print('-' * 50)
string = str(round(spline(data, x, y, z), 4))
print('|', f"{'Сплайн' : ^30}", '|', f"{string : ^13}", '|')
print('-' * 50)
string = str(round(mixed(data, x, y, z, ny), 4))
print('|', f"{'Ньютон и сплайн' : ^30}", '|', f"{string : ^13}", '|')
print('-' * 50)