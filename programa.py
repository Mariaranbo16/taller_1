#Programa para generar un número aleatorio en python

import random

#La función input() captura un dato desde el teclado 
#como si fuera una cadena de texto
a = input("Límite inferior:")
b = input("Límite superior:")

#Convertir a y b a numeros enteros, usa función int
a = int(a)
b = int(b)

respuesta = random.randint(a,b)
print (respuesta)
