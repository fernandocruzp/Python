import pyperclip, sys, random

letras='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def main():
    Mensaje= """''Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr 
 sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa 
 sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac 
 ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu 
 sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia 
 rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. 
 -Facjclxo Ctrramm"""
    miLlave= 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    Modo="decrypt"

    if not keyisvalid(miLlave):
        sys.exit("La llave elegida no sirve")

    if Modo =="encrypt":
        traduccion=encryptMessage(miLlave, Mensaje)
    elif Modo == "decrypt":
        traduccion=decryptMessage(miLlave, Mensaje)

    print('Usando la llave {}'.format(miLlave))
    print("Mensaje encryptado {}".format(traduccion))
    print("Copiado en el portapapeles")
    pyperclip.copy(traduccion)


def keyisvalid(llave):
    llavelista=list(llave)
    letrasLista= list(letras)
    llavelista.sort()
    letrasLista.sort()
    return letrasLista == llavelista

def encryptMessage(llave, mensaje):
    return traducir(llave, mensaje, 'encrypt')

def decryptMessage(llave, mensaje):
    return traducir(llave, mensaje, 'decrypt')

def traducir(llave, mensaje, modo):
    traduccion= ''
    letras1=letras
    letras2=llave
    if modo == 'decrypt':
        letras1, letras2 = letras2, letras1
    if modo== 'encrypt':
        letras1, letras2= letras1, letras2
    for i in mensaje:
        if i.upper() in letras1:
            indice=letras1.find(i.upper())
            if i.isupper():
                traduccion+=letras2[indice].upper()
            else:
                traduccion+=letras2[indice].lower()
        else:
            traduccion+=i

    return traduccion

def random():
    lista=list(letras)
    random.shuffle(lista)
    return ''.join(lista)

if __name__=='__main__':
    main()





