from newton import NewtonMethod
from spline import SplineMethod

def mixed(data, x, y, z, ny):
    zs = []
    for i in range(5):
        ys = []
        for j in range(5):
            xs = []
            for k in range(5):
                xs.append([k, data[i][j][k]])
            ys.append([j, SplineMethod(xs, x)])
        zs.append([i, NewtonMethod(ys, y, ny)])
    return SplineMethod(zs, z)