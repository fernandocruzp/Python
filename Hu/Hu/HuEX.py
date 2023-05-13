from astropy.table import QTable, Table, Column
import numpy as np
import matplotlib.pyplot as mpl
from skimage import data,io
from skimage.color import rgb2gray
from skimage.morphology import binary
#=======================================
def ExtractorHu(Ima):
    gris=rgb2gray(Ima)
    #mpl.figure(1)
    #mpl.imshow(gris, cmap='gray'
        
    binario=gris<.50 #25 #60
    #mpl.figure(2)    
    #mpl.imshow(binario, cmap='gray')
    binario=binary.binary_opening(binario)#aqui esta Op, Closing, Erosion, etc
        
    #sumafil=np.sum(binario,axis=1)#filas
    #mpl.figure(3)
    #mpl.plot(sumafil)
        
    #sumacol=np.sum(binario,axis=0)#columnas
    #mpl.figure(4)
    #mpl.plot(sumacol)
        
    ##Se obtienen los momentos de la imagen
    
    [M,N] = binario.shape
    mo=np.zeros([2,2])
    eta=np.zeros([4,4])
    n=np.zeros([4,4])
    phi=np.zeros(7)
    for p in range(2):
        for q in range(2):
            for i in range (M):
                for j in range(N):
                    mo[p,q]=mo[p,q]+((pow(i+1,p))*(pow(j+1,q))*binario[i,j])
                    ## Se obtiene momentos centrales
                    
    nx = mo[1,0] / mo[0,0]#Calculo de x negada
    ny = mo[0,1] / mo[0,0]#Calculo de y negada
    #Se realiza el calculo de los mometos centrales utilizando las formulas
    for p in range(4):
        for q in range(4):
            for i in range (M):
                for j in range(N):
                    eta[p,q]=eta[p,q]+((pow([i+1]-nx,p))*(pow([j+1]-ny,q))*binario[i,j])
    for p in range(4):
        for q in range(4):
            n[p,q]=eta[p,q]*((1/eta[0,0])**((p+q+2)/2))
    # Obtiene el momento Hu
    #Se realiza el calculo de los mometos Hu utilizando las formulas     
    phi[0] = n[2,0] + n[0,2]
    phi[1] = (n[2,0] - n[0,2])**2 + 4*n[1,1]**2;
    phi[2] = (n[3,0] - 3*n[1,2])**2 + (3*n[2,1] - n[0,3])**2
    phi[3] = (n[3,0] + n[1,2])**2 + (n[2,1] + n[0,3])**2
    phi[4] = (n[3,0] - 3*n[1,2]) * (n[3,0] + n[1,2]) *((n[3,0] + n[1,2])**2-3*(n[2,1] + n[0,3])**2)+(3*n[2,1] - n[0,3]) * (n[2,1] + n[0,3]) * (3*(n[3,0] + n[1,2])**2 - (n[2,1] + n[0,3])**2)
    phi[5] = (n[2,0] - n[0,2]) * ((n[3,0] + n[1,2])**2 - (n[2,1] + n[0,3])**2 )+4*n[1,1]*(n[3,0] + n[1,2])*(n[2,1] + n[0,3])
    phi[6] = (3*n[2,1] - n[0,3]) * (n[3,0] + n[1,2])*((n[3,0] + n[1,2])**2 - 3*(n[2,1] + n[0,3])**2 ) + (3*n[1,2] - n[3,0]) * (n[2,1]+n[0,3])*(3*(n[3,0] + n[1,2])**2 - (n[2,1] + n[0,3])**2)
    return phi,binario
#---------------------------------------
mpl.close(fig='all')

#BASE DE DATOS
M0 = np.loadtxt("Momentos0.txt")
M1 = np.loadtxt("Momentos1.txt")
M2 = np.loadtxt("Momentos2.txt")
M3 = np.loadtxt("Momentos3.txt")
M4 = np.loadtxt("Momentos4.txt")
M5 = np.loadtxt("Momentos5.txt")
M6 = np.loadtxt("Momentos6.txt")
M7 = np.loadtxt("Momentos7.txt")
M8 = np.loadtxt("Momentos8.txt")
M9 = np.loadtxt("Momentos9.txt")

Entrada=io.imread('t4.jpg')
[EntradaHu,EntradaIma]=ExtractorHu(Entrada)
mpl.figure(1)
mpl.imshow(EntradaIma,cmap='gray')

print('Momentos Base de Datos')
t = Table(rows=[M0[0:5],M1[0:5],M2[0:5],M3[0:5],M4[0:5],M5[0:5],M6[0:5],M7[0:5],M8[0:5],M9[0:5],[0,0,0,0,0],EntradaHu[0:5]],names=('Q1','Q2','Q3','Q4','Q5'))
print(t)

#IDENTIFICADOR
I0=abs(EntradaHu[4]-M0[4])
I1=abs(EntradaHu[4]-M1[4])
I2=abs(EntradaHu[4]-M2[4])
I3=abs(EntradaHu[4]-M3[4])
I4=abs(EntradaHu[4]-M4[4])
I5=abs(EntradaHu[4]-M5[4])
I6=abs(EntradaHu[4]-M6[4])
I7=abs(EntradaHu[4]-M7[4])
I8=abs(EntradaHu[4]-M8[4])
I9=abs(EntradaHu[4]-M9[4])
ID=[I0,I1,I2,I3,I4,I5,I6,I7,I8,I9]
PosMin=np.argmin(ID)
print('Es el número:     ')
print(PosMin)