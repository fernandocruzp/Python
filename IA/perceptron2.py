import numpy as np
import matplotlib.pyplot as mpl

p = np.array(([0,0,1,1],[0,1,0,1]))
w = [0.5,0.5]
b = -0.25
b2 = -0.75

def HardLim(n):
    if(n<0): a =0
    else: a =1
    return a

[i,r] = p.shape
for j in range(r):
    pp = p[:,j]
    n1 = np.dot(w,pp) + b
    n2 = np.dot(w,pp) + b2
    a1 = HardLim(n1)
    a2 = HardLim(n2)
    print('patron',pp)
    print('salida',a1,a2)
    mpl.figure(1)
    mpl.grid(True)
    mpl.scatter(pp[0], pp[1])
    
x = np.linspace(-2,2,100)
y = -x + 0.5
y2 = -x + 1.5
mpl.figure(1)
mpl.plot(x, y)
mpl.plot(x, y2)


for i in np.arange(-2,2,0.2):
    for j in np.arange(-2,2,0.2):
        pp = [i,j]
        n = np.dot(w,pp) + b
        a = HardLim(n)
        n2 = np.dot(w,pp) + b2
        a2 = HardLim(n2)
        mpl.figure(2)
        mpl.grid(True)
        if (a == a2): mpl.scatter(pp[0], pp[1], c = 'g')
        else: mpl.scatter(pp[0], pp[1], c = 'b')