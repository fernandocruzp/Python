#!/usr/bin/env python
# coding: utf-8
letras = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
abecedario = letras + letras.lower() + '\t\n' + ' '


# In[4]:


def cargar():
    #g = open('dictionary.txt')
    g = open('listado-general.txt', encoding='utf-8')
    palabras_espa = {}
    for palabra in g.read().split('\n'):
        palabras_espa[palabra]=None
    g.close()
    return palabras_espa


# In[5]:


def noletras(mensaje):
    letras =[]
    for letra in mensaje:
        if letra in abecedario:
            letras.append(letra)
    return ''.join(letras)


# In[8]:

diccionario = cargar()
def contarpalabras(mensaje):
    mensaje = mensaje.lower()
    mensaje = noletras(mensaje)
    palabras = mensaje.split()
    if palabras == []:
        return 0.0
    matches = 0
    for palabra in palabras:
        if palabra in diccionario:
            matches += 1
    return float(matches)/len(palabras)


# In[9]:


def espanol(mensaje, porcentajepa = 40, porcentajelet = 85):
    palabras_esp = contarpalabras(mensaje)*100 >= porcentajepa
    numeroletras = len(noletras(mensaje))
    porceletras = float(numeroletras)/len(mensaje) * 100
    letras_Esp = porceletras >= porcentajelet
    return palabras_esp and letras_Esp


# In[ ]:
print(espanol("hola my name es bruno"))