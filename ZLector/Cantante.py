import pyttsx3

habla = pyttsx3.init()
f = open("C:\\Users\cruzf\\PycharmProjects\\ZLector de Texto\\ZLector de Texto\\verso.txt","r")
Texto = f.read()
print(Texto)
f.close()
#voz = habla.getProperty('voz')      
#engine.setProperty('habla', voices[1].id)
habla.setProperty('rate', 96)
habla.say(Texto)
habla.runAndWait()
    
