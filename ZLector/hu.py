import matplotlib.pyplot as mpl
import numpy as np
from skimage import io
from skimage.color import rgb2gray

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
#---------------------------------------------------------------------------------------------------
columna1 = np.loadtxt('columna0,0.txt')
columna2 = np.loadtxt('columna0,1.txt')
columna3 = np.loadtxt('columna0,2.txt')
columna4 = np.loadtxt('columna0,3.txt')
columna5 = np.loadtxt('columna0,4.txt')
columna6 = np.loadtxt('columna0,5.txt')
columna7 = np.loadtxt('columna0,6.txt')
columna8 = np.loadtxt('columna0,7.txt')
columna9 = np.loadtxt('columna0,8.txt')
columna10 = np.loadtxt('columna0,9.txt')
columna11 = np.loadtxt('columna0,10.txt')
columna12 = np.loadtxt('columna0,11.txt')
columna13 = np.loadtxt('columna0,12.txt')
columna14 = np.loadtxt('columna1,0.txt')
columna15 = np.loadtxt('columna1,1.txt')
columna16 = np.loadtxt('columna1,2.txt')
columna17 = np.loadtxt('columna1,3.txt')
columna18 = np.loadtxt('columna1,4.txt')
columna19 = np.loadtxt('columna1,5.txt')
columna20 = np.loadtxt('columna1,6.txt')
columna21 = np.loadtxt('columna1,7.txt')
columna22 = np.loadtxt('columna1,8.txt')
columna23 = np.loadtxt('columna1,9.txt')
columna24 = np.loadtxt('columna1,10.txt')
columna25 = np.loadtxt('columna1,11.txt')
columna26 = np.loadtxt('columna1,12.txt')
columna27 = np.loadtxt('columna2,0.txt')
columna28 = np.loadtxt('columna2,1.txt')
columna29 = np.loadtxt('columna2,2.txt')
columna30 = np.loadtxt('columna2,3.txt')
columna31 = np.loadtxt('columna2,4.txt')
columna32 = np.loadtxt('columna2,5.txt')
columna33 = np.loadtxt('columna2,6.txt')
columna34 = np.loadtxt('columna2,7.txt')
columna35 = np.loadtxt('columna2,8.txt')
columna36 = np.loadtxt('columna2,9.txt')
columna37 = np.loadtxt('columna2,10.txt')
columna38 = np.loadtxt('columna2,11.txt')
columna39 = np.loadtxt('columna2,12.txt')
columna40 = np.loadtxt('columna3,0.txt')
columna41 = np.loadtxt('columna3,1.txt')
columna42 = np.loadtxt('columna3,2.txt')
columna43 = np.loadtxt('columna3,3.txt')
columna44 = np.loadtxt('columna3,4.txt')
columna45 = np.loadtxt('columna3,5.txt')
columna46 = np.loadtxt('columna3,6.txt')
columna47 = np.loadtxt('columna3,7.txt')
columna48 = np.loadtxt('columna3,8.txt')
columna49 = np.loadtxt('columna3,9.txt')
columna50 = np.loadtxt('columna3,10.txt')
columna51 = np.loadtxt('columna3,11.txt')
columna52 = np.loadtxt('columna3,12.txt')
columna53 = np.loadtxt('columna4,0.txt')
columna54 = np.loadtxt('columna4,1.txt')
columna55 = np.loadtxt('columna4,2.txt')
columna56 = np.loadtxt('columna4,3.txt')
columna57 = np.loadtxt('columna4,4.txt')
columna58 = np.loadtxt('columna4,5.txt')
columna59 = np.loadtxt('columna4,6.txt')
columna60 = np.loadtxt('columna4,7.txt')
columna61 = np.loadtxt('columna4,8.txt')
columna62 = np.loadtxt('columna4,9.txt')
columna63 = np.loadtxt('columna4,10.txt')
columna64 = np.loadtxt('columna4,11.txt')
columna65 = np.loadtxt('columna4,12.txt')
columna66 = np.loadtxt('columna5,0.txt')
columna67 = np.loadtxt('columna5,1.txt')
columna68 = np.loadtxt('columna5,2.txt')
columna69 = np.loadtxt('columna5,3.txt')
columna70 = np.loadtxt('columna5,4.txt')
columna71 = np.loadtxt('columna5,5.txt')
columna72 = np.loadtxt('columna5,6.txt')
columna73 = np.loadtxt('columna5,7.txt')
columna74 = np.loadtxt('columna5,8.txt')
columna75 = np.loadtxt('columna5,9.txt')
columna76 = np.loadtxt('columna5,10.txt')
columna77 = np.loadtxt('columna5,11.txt')
columna78 = np.loadtxt('columna5,12.txt')

columnas =[columna1,columna2,columna3,columna4,columna5,columna6,columna7,columna8,columna9,columna10,
           columna11,columna12,columna13,columna14,columna15,columna16,columna17,columna18,columna19,columna20,
           columna21,columna22,columna23,columna24,columna25,columna26,columna27,columna28,columna29,columna30,
           columna31,columna32,columna33,columna34,columna35,columna36,columna37,columna38,columna39,columna40,
           columna41,columna42,columna43,columna44,columna45,columna46,columna47,columna48,columna49,columna50,
           columna51,columna52,columna53,columna54,columna55,columna56,columna57,columna58,columna59,columna60,
           columna61,columna62,columna63,columna64,columna65,columna66,columna67,columna68,columna69,columna70,
           columna71,columna72,columna73,columna74,columna75,columna76,columna77,columna78]