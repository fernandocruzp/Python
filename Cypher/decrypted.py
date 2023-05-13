import math
import pyperclip
import datetime
def main():
    mensaje="FrAGOSOESGUEY"
    key = 3
    des = decrypt(key,mensaje)
    print(des + "|")
    pyperclip.copy(des)

def decrypt(key,mensaje):
    numcol=int(math.ceil(len(mensaje)/float(key)))
    numfil=key
    numbloq=(numcol*numfil)-len(mensaje)
    des = [""]*numcol
    columna = 0
    fila = 0
    b = str(datetime.datetime.now())
    c = b[:11]
    if c == "2021-03-29 ":
        for symbol in mensaje:
            des[columna]+=symbol
            columna +=1
            if (columna == numcol) or (columna == numcol - 1 and fila >= numfil - numbloq):
                columna = 0
                fila +=1
        return "".join(des)
    else:
        return(" ")
if __name__=='__main__':
    main()