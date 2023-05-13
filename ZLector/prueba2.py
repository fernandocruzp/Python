import numpy as np
from scipy import stats
import pyttsx3


M = []
for i in range(64):
    M.append(np.loadtxt("Momento{}".format(i)))
C  = []   
for j in range(24):
    C.append(np.loadtxt("Cancion{}".format(j)))
#M.append(np.loadtxt("Momentoa"))
cancion = []
count1 = []
for i in range(len(C)):
    ID= []
    ID2= []
    ID3= []
    ID4= []
    ID5= []
    ID6= []
    ID7= []
    Posmin1 = []
    Posmin = 0;
    for j in range(len(M)):
        ID.append(abs(C[i][0]-M[j][0]))
        ID2.append(abs(C[i][1]-M[j][1]))
        ID3.append(abs(C[i][2]-M[j][2]))
        ID4.append(abs(C[i][3]-M[j][3]))
        ID5.append(abs(C[i][4]-M[j][4]))
        ID6.append(abs(C[i][5]-M[j][5]))
        ID7.append(abs(C[i][6]-M[j][6]))
    Posmin1 = [np.argmin(ID), np.argmin(ID2), np.argmin(ID3), np.argmin(ID4), np.argmin(ID5), np.argmin(ID6), np.argmin(ID7)]    
    Posmin,count = stats.mode(np.array(Posmin1))
    count1.append(count)
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
                cancion.append('a')
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

#cancion.pop(30)
#cancion.insert(30, 'u')
print(cancion)
stra = "".join(cancion)
print(stra)
habla = pyttsx3.init()
#voz = habla.getProperty('voz')      
#engine.setProperty('habla', voices[1].id)
habla.setProperty('rate', 110)
habla.say(stra)
habla.runAndWait()

"""f = open("C:\\Users\cruzf\\PycharmProjects\\ZLector de Texto\\ZLector de Texto\\verso.txt","a")
f.write(stra + " ")
f.close()
"""