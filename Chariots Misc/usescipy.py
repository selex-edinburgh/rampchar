from scipy.optimize import fsolve

def equations(p):
    x, y = p
    return (R1**2 - (X-Xpole1)**2 - (Y-Ypole1)**2, R2**2 -(X-Xpole2)**2 - (Y-Ypole2)**2)

if __name__ == '__main__':
    
    x, y =  fsolve(equations, (1400, 2000))     
    print equations((x, y))
