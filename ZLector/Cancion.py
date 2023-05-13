import matplotlib.pyplot as mpl
import numpy as np
from skimage import io
from skimage.color import rgb2gray
import pyttsx3
#---------------------------------
"""M = []
M.append(np.loadtxt("Momento00")); M.append(np.loadtxt("Momento01")); M.append(np.loadtxt("Momento02")); M.append(np.loadtxt("Momento03")); M.append(np.loadtxt("Momento04")); M.append(np.loadtxt("Momento05")); M.append(np.loadtxt("Momento06")); M.append(np.loadtxt("Momento07"))
M.append(np.loadtxt("Momento08")); M.append(np.loadtxt("Momento09")); M.append(np.loadtxt("Momento010")); M.append(np.loadtxt("Momento011")); M.append(np.loadtxt("Momento012")); M.append(np.loadtxt("Momento013")); M.append(np.loadtxt("Momento10")); M.append(np.loadtxt("Momento11"))
M.append(np.loadtxt("Momento12")); M.append(np.loadtxt("Momento13")); M.append(np.loadtxt("Momento14")); M.append(np.loadtxt("Momento15")); M.append(np.loadtxt("Momento16")); M.append(np.loadtxt("Momento17")); M.append(np.loadtxt("Momento18")); M.append(np.loadtxt("Momento19"))
M.append(np.loadtxt("Momento110")); M.append(np.loadtxt("Momento111")); M.append(np.loadtxt("Momento112")); M.append(np.loadtxt("Momento20")); M.append(np.loadtxt("Momento21")); M.append(np.loadtxt("Momento22")); M.append(np.loadtxt("Momento23")); M.append(np.loadtxt("Momento24"))
M.append(np.loadtxt("Momento25")); M.append(np.loadtxt("Momento26")); M.append(np.loadtxt("Momento27")); M.append(np.loadtxt("Momento28")); M.append(np.loadtxt("Momento29")); M.append(np.loadtxt("Momento210")); M.append(np.loadtxt("Momento211")); M.append(np.loadtxt("Momento212"))
M.append(np.loadtxt("Momento40")); M.append(np.loadtxt("Momento42")); M.append(np.loadtxt("Momento43")); M.append(np.loadtxt("Momento44")); M.append(np.loadtxt("Momento45")); M.append(np.loadtxt("Momento46"))
M.append(np.loadtxt("Momento47")); M.append(np.loadtxt("Momento48")); M.append(np.loadtxt("Momento49")); M.append(np.loadtxt("Momento410")); M.append(np.loadtxt("Momento411")); M.append(np.loadtxt("Momento50")); M.append(np.loadtxt("Momento51")); M.append(np.loadtxt("Momento52"))
M.append(np.loadtxt("Momento53")); M.append(np.loadtxt("Momento54")); M.append(np.loadtxt("Momento55")); M.append(np.loadtxt("Momento56")); M.append(np.loadtxt("Momento57")); M.append(np.loadtxt("Momento58")); M.append(np.loadtxt("Momento59")); M.append(np.loadtxt("Momento510"))
M.append(np.loadtxt("Momento511")); M.append(np.loadtxt("Momento512")); M.append(np.loadtxt("Momento513"))
"""
#----------------------------------------
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
Ima = io.imread("Ciudad4.jpg")
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
    if(sumafil[i] > 5 and a == 0):
        inicio = i; a = 1;
    if (sumafil[i] < 5 and a == 1):
        final = i; a = 0
        renglon = bina[inicio:final,:]
        renglones.append(renglon)
        cont +=1

"""sumafil1 = np.sum(renglon, axis = 1)
mpl.subplot(1,2,2)
mpl.plot(sumafil1)"""
columnas = []
cancion = []
for k in range(len(renglones)):
    [fila,colu] = renglones[k].shape
    sumacol = np.sum(renglones[k], axis = 0)
    mpl.figure(5)
    mpl.plot(sumacol)
    a = 0
    m = 0
    for i in range(colu):
        if(sumacol[i] > 5 and a == 0):
            inicio1 = i; a = 1
        if(sumacol[i] < 6 and a == 1 ):
            final1 = i; a = 0
            columna = renglones[k][:,inicio1:final1]
            columnas.append(columna)
            #momento = ExtractorHu(columna)
            m = m +1
            ID = []
            """for j in range(len(M)):
                ID.append(abs(momento[4]-M[j][4]))
            
            Posmin = np.argmin(ID)
            if(Posmin == 0):
                cancion.append('a')
            elif(Posmin == 1):
                cancion.append('b')
            elif(Posmin == 2):
                cancion.append('c')
            elif(Posmin == 3):
                cancion.append('d')
            elif(Posmin == 4):
                cancion.append('e')
            elif(Posmin == 5):
                cancion.append('f')
            elif(Posmin == 6):
                cancion.append('g')
            elif(Posmin == 7):
                cancion.append('h')
            elif(Posmin == 8):
                cancion.append('i')
            elif(Posmin == 9):
                cancion.append('j')
            elif(Posmin == 10):
                cancion.append('k')
            elif(Posmin == 11):
                cancion.append('l')
            elif(Posmin == 12):
                cancion.append('m')
            elif(Posmin == 13):
                cancion.append('n')
            elif(Posmin == 14):
                cancion.append('ñ')                
            elif(Posmin == 15):
                cancion.append('o')
            elif(Posmin == 16):
                cancion.append('p')
            elif(Posmin == 17):
                cancion.append('q')
            elif(Posmin == 18):
                cancion.append('r')
            elif(Posmin == 19):
                cancion.append('s')
            elif(Posmin == 20):
                cancion.append('t')
            elif(Posmin == 21):
                cancion.append('u')
            elif(Posmin == 22):
                cancion.append('v')
            elif(Posmin == 23):
                cancion.append('w')
            elif(Posmin == 24):
                cancion.append('x')
            elif(Posmin == 25):
                cancion.append('y')
            elif(Posmin == 26):
                cancion.append('z')
            elif(Posmin == 27):
                cancion.append('A')
            elif(Posmin == 28):
                cancion.append('B')
            elif(Posmin == 29):
                cancion.append('C')
            elif(Posmin == 30):
                cancion.append('D')
            elif(Posmin == 31):
                cancion.append('E')
            elif(Posmin == 32):
                cancion.append('F')
            elif(Posmin == 33):
                cancion.append('G')
            elif(Posmin == 34):
                cancion.append('H')
            elif(Posmin == 35):
                cancion.append('I')
            elif(Posmin == 36):
                cancion.append('J')
            elif(Posmin == 37):
                cancion.append('K')
            elif(Posmin == 38):
                cancion.append('L')
            elif(Posmin == 39):
                cancion.append('M')
            elif(Posmin == 40):
                cancion.append('N')
            elif(Posmin == 41):
                cancion.append('O')
            elif(Posmin == 42):
                cancion.append('P')
            elif(Posmin == 43):
                cancion.append('Q')
            elif(Posmin == 44):
                cancion.append('R')
            elif(Posmin == 45):
                cancion.append('S')
            elif(Posmin == 46):
                cancion.append('T')
            elif(Posmin == 47):
                cancion.append('U')
            elif(Posmin == 48):
                cancion.append('V')
            elif(Posmin == 49):
                cancion.append('W')
            elif(Posmin == 50):
                cancion.append('X')
            elif(Posmin == 51):
                cancion.append('Y')
            elif(Posmin == 52):
                cancion.append('Z')
            elif(Posmin == 53):
                cancion.append('0')
            elif(Posmin == 54):
                cancion.append('1')
            elif(Posmin == 55):
                cancion.append('2')
            elif(Posmin == 56):
                cancion.append('3')
            elif(Posmin == 57):
                cancion.append('4')
            elif(Posmin == 58):
                cancion.append('5')
            elif(Posmin == 59):
                cancion.append('6')
            elif(Posmin == 60):
                cancion.append('7')
            elif(Posmin == 61):
                cancion.append('8')
            elif(Posmin == 62):
                cancion.append('9')
            elif(Posmin == 63):
                cancion.append('.')
            elif(Posmin == 64):
                cancion.append(',')              """
mpl.figure(6)
mpl.imshow(columnas[134], cmap = 'gray')

print(cancion)
"""    for i in range(len(columnas)):
        np.savetxt('columna{},{}'.format(k,i), columnas[i])
"""        
"""stra = "".join(cancion)
habla = pyttsx3.init()
habla.say(stra)
habla.runAndWait()"""