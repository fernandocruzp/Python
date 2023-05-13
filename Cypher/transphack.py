import Español as esp, decrypted, pyperclip
def main():
    mensaje ="""MPo e jioessals  dTesrs.a n umdee  a ilon eed soqeua adaneeyhlqu  r  rí cyoao e  lactaie lvanasl dognos  u e d ero d a uncmtleq po  m dsáY  oannblaem m.oaitotsetdet eear .lrqbpetaeoonuvambabpe ropl rdoea.oiyi sltrsr. ee iis   eloula os  s eeliegiá eb aaddo r   g gC  eo e vmlpercmaala iarh adt e.ooebuéjcnovrsee leeAaoaooje smtLap on uúp  myerqaa.iodl  mnianao loq  ,tossl    nusy ueu rpreaesrtpo r uy  vdí Alade. rlleyucl es clmJmL ec jynimaaq  lieoi hode mYioaplason vooos eiacr duíiuiuegoau isánruqlacnca"""
    mensajedecr = hack(mensaje)
    if mensajedecr == None:
        print('Fallé lo siento')
    else:
        print(mensajedecr)
        pyperclip.copy(mensajedecr)

def hack(mensaje):
    for i in range(1, len(mensaje)):
        print('Intentando clave {}....'.format(i))
        texto = decrypted.decrypt(i, mensaje)
        if esp.espanol(texto):
            print('Posible respuesta')
            print('Clave: {} :{}'.format(i,texto[:100]))
            respuesta = input('Es la respuesta que busca? S/N ')
            if respuesta.strip().upper().startswith('S'):
                return texto
    return None
if __name__ == '__main__':
    main()