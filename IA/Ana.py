import pyttsx3 as voz
import speech_recognition as sp
import subprocess
import webbrowser
from datetime import datetime


voce=voz.init()
voces = voce.getProperty('voices')
voce.setProperty('voice',voces[0].id)
voce.setProperty('rate', 140)

def habla(texto):
    voce.say(texto)
    voce.runAndWait()

while True:
    recog = sp.Recognizer()

    with sp.Microphone() as source:
        print('Escuchando...')
        audio=recog.listen(source)

    try:
        orden = recog.recognize_google(audio, language='es-MX')
        orden=orden.lower()
        orden=orden.split(' ')
        print(orden)
        if 'ana' in orden or 'anna':
            orden.pop(0)
            if 'abre' in orden or 'abrir' in orden:
                    sitios={
                        'google':'google.com',
                        'youtube':'youtube.com',
                        'twitter':'twitter.com',
                        'facebook':'facebook.com',
                        'instagram':'instagram.com',
                        'spotify':'open.spotify.com',


                    }
                    for i in list(sitios.keys()):
                        if i in orden:
                            print(sitios[i])
                            subprocess.call(f'start Chrome.exe {sitios[i]}', shell=True)
                            habla('Abriendo {}'.format(i))

            elif 'hora' in orden:
                hora=datetime.now().strftime('%H:%M')
                habla('Son las {}'.format(hora))

            elif 'qué' in orden or 'cuál' in orden or 'busca' in orden or 'cuánto' in orden or 'buscar' in orden:
                if 'busca' in orden:
                    orden.pop(0)
                orden = "+".join(orden)
                print(orden)
                busqueda='google.com/search?q={}'.format(orden)
                print(busqueda)
                subprocess.call(f'start Chrome.exe {busqueda}', shell=True)
                habla('Buscando {}'.format(orden))

            elif 'anota' in orden or 'escribe' in orden:
                print('si')
                orden[0]=""
                orden= " ".join(orden)
                print(orden)
                orden.replace('anota','')
                orden.replace('escribe','')
                f = open('C:\\Users\\cruzf\\PycharmProjects\\pythonProject1\\Nota.txt', 'a')
                f.write('\n')
                f.write(orden)

            elif 'correo' in orden:
                busqueda="mail.google.com/mail/u/0/?tab=rm&ogbl"
                print(busqueda)
                subprocess.call(f'start Chrome.exe {busqueda}', shell=True)
                habla('revisando tu correo')

            elif 'lee' in orden or 'notas' in orden:
                f = open('C:\\Users\\cruzf\\PycharmProjects\\pythonProject1\\Nota.txt', 'r')
                texto= f.read()
                f.close()
                habla("Tus notas son" + texto)

            elif 'adios' in orden or 'termina' in orden or 'terminado' in orden:
                habla('Adios Fernando')
                break
    except:
        print('No entendí lo que dijiste, vuelve a intentar')


