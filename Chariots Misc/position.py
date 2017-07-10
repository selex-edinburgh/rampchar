import math
import scipy.optimize

def f(x1, y1, r1, x2, y2, r2, p, q) :
    return [r1**2 - (x1-p)**2 - (y1-q)**2, r2**2 - (x2-p)**2 - (y2-q)**2]

print scipy.optimize(f, (2, 2, 1, 2.5, 1.5, 1, 2,1))
