#regla instar
import numpy as np
import math

def HardLim(n):
    if(n<0): a = 0
    else: a=1
    return a


W=np.array([[ 12, 10, 25, 13, 27]]) #Patron Original

Pt=np.array([[12],[10],[25],[10],[27]]) #patron modificado

Wn = np.linalg.norm(W)
Pnt = np.linalg.norm(Pt)
#Valor de theta

theta = (math.pi)/6

b = -(Wn*Pnt*(math.cos(theta)))
n = np.dot(W,Pt) + b
a = HardLim(n)
print('a = ' , a)
