import numpy as np
from numpy import sin, cos,acos,asin,atan2,sqrt

a1 = 0.138
a2 = 0.106
a3 = 0.115
a4 = 0.19
def InverseKinematics(x,y,z):
    r1 = sqrt(x**2 + y**2)
    T1 = atan2(y,x)
    r2 = z -a1
    r = sqrt(r1**2 + r2**2)
    beta = atan2(r2,r1)
    alpha = acos((r**2 + a2**2 - a3**2)/(2*r*a2))
    T2 = beta + alpha
    gamma = acos((a3**2 + a2**2 - r**2)/(2*a2*a3))
    T3 = np.pi - gamma
    
    return T1, T2, T3

T1, T2, T3 = InverseKinematics(0.106,0,0.138)
print(np.rad2deg(T1), np.rad2deg(T2), np.rad2deg(T3))