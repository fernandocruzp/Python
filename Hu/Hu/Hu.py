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
        
    binario=gris<.5 #25 #60
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
    phi[4] = (n[3,0] - 3*n[1,2]) * (n[3,0] + n[1,2]) * ((n[3,0] + n[1,2])**2-3*(n[2,1] + n[0,3])**2)+(3*n[2,1] - n[0,3]) * (n[2,1] + n[0,3]) * (3*(n[3,0] + n[1,2])**2 - (n[2,1] + n[0,3])**2)
    phi[5] = (n[2,0] - n[0,2]) * ((n[3,0] + n[1,2])**2 - (n[2,1] + n[0,3])**2 )+4*n[1,1]*(n[3,0] + n[1,2])*(n[2,1] + n[0,3])
    phi[6] = (3*n[2,1] - n[0,3]) * (n[3,0] + n[1,2])*((n[3,0] + n[1,2])**2 - 3*(n[2,1] + n[0,3])**2 ) + (3*n[1,2] - n[3,0]) * (n[2,1]+n[0,3])*(3*(n[3,0] + n[1,2])**2 - (n[2,1] + n[0,3])**2)
    return phi,binario
#---------------------------------------
mpl.close(fig='all')

#BASE DE DATOS

Ima0=io.imread('0.jpg')
Ima1=io.imread('1.jpg')
Ima2=io.imread('2.jpg')
Ima3=io.imread('3.jpg')
Ima4=io.imread('4.jpg')
Ima5=io.imread('5.jpg')
Ima6=io.imread('6.jpg')
Ima7=io.imread('7.jpg')
Ima8=io.imread('8.jpg')
Ima9=io.imread('9.jpg')

Entrada=io.imread('try5.jpg')
[EntradaHu,EntradaIma]=ExtractorHu(Entrada)
print('momentos entrada')
print(EntradaHu)

for k in range(10):
    if(k==0): Ima=Ima0
    if(k==1): Ima=Ima1
    if(k==2): Ima=Ima2
    if(k==3): Ima=Ima3
    if(k==4): Ima=Ima4
    if(k==5): Ima=Ima5
    if(k==6): Ima=Ima6
    if(k==7): Ima=Ima7
    if(k==8): Ima=Ima8
    if(k==9): Ima=Ima9
    
    [momentos,grafica]=ExtractorHu(Ima)
                            
    if(k==0): P0=grafica; M0=momentos; np.savetxt("Momentos0.txt", M0)
    if(k==1): P1=grafica; M1=momentos; np.savetxt("Momentos1.txt", M1)
    if(k==2): P2=grafica; M2=momentos; np.savetxt("Momentos2.txt", M2)
    if(k==3): P3=grafica; M3=momentos; np.savetxt("Momentos3.txt", M3)
    if(k==4): P4=grafica; M4=momentos; np.savetxt("Momentos4.txt", M4)
    if(k==5): P5=grafica; M5=momentos; np.savetxt("Momentos5.txt", M5)
    if(k==6): P6=grafica; M6=momentos; np.savetxt("Momentos6.txt", M6)
    if(k==7): P7=grafica; M7=momentos; np.savetxt("Momentos7.txt", M7)
    if(k==8): P8=grafica; M8=momentos; np.savetxt("Momentos8.txt", M8)
    if(k==9): P9=grafica; M9=momentos; np.savetxt("Momentos9.txt", M9)
    
mpl.figure(5)
mpl.subplot(5,2,1)
mpl.title('0')   
io.imshow(P0)
mpl.subplot(5,2,2)  
mpl.title('1')     
io.imshow(P1)
mpl.subplot(5,2,3) 
mpl.title('2')      
io.imshow(P2)
mpl.subplot(5,2,4) 
mpl.title('3')      
io.imshow(P3)
mpl.subplot(5,2,5)
mpl.title('4')       
io.imshow(P4)
mpl.subplot(5,2,6)  
mpl.title('5')     
io.imshow(P5)
mpl.subplot(5,2,7)
mpl.title('6')       
io.imshow(P6)
mpl.subplot(5,2,8)    
mpl.title('7')   
io.imshow(P7)
mpl.subplot(5,2,9)    
mpl.title('8')   
io.imshow(P8)
mpl.subplot(5,2,10)    
mpl.title('9')   
io.imshow(P9)

print('Momentos Base de Datos')
print(M0)
print(M1)
print(M2)
print(M3)
print(M4)
print(M5)
print(M6)
print(M7)
print(M8)
print(M9)