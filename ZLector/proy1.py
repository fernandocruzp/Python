import matplotlib.pyplot as mpl
import numpy as np
from skimage import io
from skimage.color import rgb2gray
#---------------------------------
def ExtractorHu(columna):

    [M,N] = columna.shape
    mo=np.zeros([2,2])
    eta=np.zeros([4,4])
    n=np.zeros([4,4])
    phi=np.zeros(7)
    for p in range(2):
        for q in range(2):
            for i in range (M):
                for j in range(N):
                    mo[p,q]=mo[p,q]+((pow(i+1,p))*(pow(j+1,q))*columna[i,j])
                    ## Se obtiene momentos centrales
                    
    nx = mo[1,0] / mo[0,0]#Calculo de x negada
    ny = mo[0,1] / mo[0,0]#Calculo de y negada
    #Se realiza el calculo de los mometos centrales utilizando las formulas
    for p in range(4):
        for q in range(4):
            for i in range (M):
                for j in range(N):
                    eta[p,q]=eta[p,q]+((pow([i+1]-nx,p))*(pow([j+1]-ny,q))*columna[i,j])
    for p in range(4):
        for q in range(4):
            n[p,q]=eta[p,q]*((1/eta[0,0])**((p+q+2)/2))
    # Obtiene el momento Hu
    #Se realiza el calculo de los mometos Hu utilizando las formulas     
    phi[0] = n[2,0] + n[0,2]
    phi[1] = (n[2,0] - n[0,2])**2 + 4*n[1,1]**2;
    phi[2] = (n[3,0] - 3*n[1,2])**2 + (3*n[2,1] - n[0,3])**2
    phi[3] = (n[3,0] + n[1,2])**2 + (n[2,1] + n[0,3])**2
    phi[4] = (n[3,0] - 3*n[1,2]) * (n[3,0] + n[1,2]) * ((n[3,0] + n[1,2])**2-3*(n[2,1] + n[0,3])**2)+(3*n[2,1] - n[0,3]) * (n[2,1] + n[0,3]) * (3*(n[3,0] + n[1,2])**2 - (n[2,1] + n[0,3])**2)
    phi[5] = (n[2,0] - n[0,2]) * ((n[3,0] + n[1,2])**2 - (n[2,1] + n[0,3])**2 )+4*n[1,1]*(n[3,0] + n[1,2])*(n[2,1] + n[0,3])
    phi[6] = (3*n[2,1] - n[0,3]) * (n[3,0] + n[1,2])*((n[3,0] + n[1,2])**2 - 3*(n[2,1] + n[0,3])**2 ) + (3*n[1,2] - n[3,0]) * (n[2,1]+n[0,3])*(3*(n[3,0] + n[1,2])**2 - (n[2,1] + n[0,3])**2)
    return phi
#-------------------------------------------------------------------------------------------
mpl.close('all')
Ima = io.imread("Ciudad5.jpg")
mpl.figure(1)
mpl.imshow(Ima)
ImaG = rgb2gray(Ima)
bina = ImaG < 0.5
mpl.figure(2)
mpl.imshow(bina, cmap = 'gray')

sumafil = np.sum(bina,axis=1)
mpl.figure(3)
mpl.plot(sumafil)

[fil,col] = bina.shape
a = 0; cont = 0
renglones = []
for i in range(fil):
    if(sumafil[i] > 3 and a == 0):
        inicio = i; a = 1;
    if (sumafil[i] < 3 and a == 1):
        final = i; a = 0
        renglon = bina[inicio:final,:]
        renglones.append(renglon)
        cont +=1
        
mpl.figure(8)
mpl.imshow(renglones[0], cmap = 'gray')
sumacol = np.sum(renglones[1], axis = 0)
mpl.figure(5)
mpl.subplot(1, 2,1)
mpl.plot(sumacol)

sumafil1 = np.sum(renglon, axis = 1)
mpl.subplot(1,2,2)
mpl.plot(sumafil1)
columnas = []
m = 0
for k in range(len(renglones)):
    sumacol = np.sum(renglones[k], axis = 0)
    mpl.figure(5)
    mpl.plot(sumacol)
    [fila,colu] = renglones[k].shape
    a = 0
    for i in range(colu):
        if(sumacol[i] > 5 and a == 0):
            inicio1 = i; a = 1
        if(sumacol[i] < 3 and a == 1 ):
            final1 = i; a = 0
            columna = renglones[k][:,inicio1:final1]
            #momento = ExtractorHu(columna)
            #np.savetxt("Cancion{}".format(m), momento)
            m = m +1
            columnas.append(columna)
mpl.figure(6)
mpl.imshow(columnas[442], cmap = 'gray')

#np.savetxt("Momentos",columnas)

"""    for i in range(len(columnas)):
        np.savetxt('columna{},{}'.format(k,i), columnas[i])
"""        