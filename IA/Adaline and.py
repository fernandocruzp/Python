#adaline
import matplotlib.pyplot as mpl
import numpy as np
mpl.close(fig='all')
P = np.array(([0,0,1,1],[0,1,0,1]))
t = np.array(([0,0,0,1]))
s = 1
[R,k] = P.shape
W = np.random.rand(s,R)
B = np.random.rand(s,1)
alpha = 0.8
ep = 10

def HardLim(n):
    if(n<0): a = 0
    else: a = 1
    return a

mpl.figure(1)
mpl.subplot(1,2,1)
mpl.xlim([-3,3])
mpl.ylim([-3,3])
mpl.title("Puntos AND")
mpl.grid()
mpl.scatter(P[0,:],P[1,:])
mpl.subplot(1,2,2)
mpl.xlim([-3,3])
mpl.ylim([-3,3])
mpl.title("Evaluación de n puntos")

for e in range(ep):
    for j in range(k):
        PP = P[:,j]
        n = np.dot(W,PP) + B #n = w*p+b
        a = HardLim(n)
        #Calculo del error
        e = t[j] - a
        #Aprendizaje
        W = W + alpha*e*PP
        B = B + alpha*e
        print(a)    
    print('==================')
    print(W)
    print(B)
    mW=(0-W[0,1])/(0-W[0,0]) #m=dy/dx
    m = -1/mW
    b = -B/W[0,1]
    x=np.linspace(-3,3,50)
    y=np.reshape(m*x+b,[50,])
    mpl.subplot(1,2,1)
    mpl.plot(x,y)
    mpl.pause(3)
    
    for i in np.arange(-3,3, .2):
        for j in np.arange(-3,3,.2):
            PP = [i,j]
            n = np.dot(W,PP) + B
            a = HardLim(n)
            if(a==0):
                mpl.subplot(1,2,2)
                mpl.scatter(PP[0],PP[1],c = 'r')
            else:
                mpl.subplot(1,2,2)
                mpl.scatter(PP[0],PP[1],c = 'b')
    mpl.subplot(1,2,2)
    mpl.scatter(P[0,:],P[1,:], c = 'g')
    mpl.pause(3)
    