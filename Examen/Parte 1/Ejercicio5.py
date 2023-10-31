# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 10:34:39 2023

@author: agonjur
"""

#Ejercicio 5

adivinaNumero = 56
numero_intro = int(input("Introduzca un número:"))
#Pongo que el contador empiece en 1, para que cuente 
#como intento también el que acierte.
contador = 1
while adivinaNumero != numero_intro:
    if adivinaNumero > numero_intro:
        print("El numero introducido es menor que el que hay que adivinar.")
    else:
        print("El numero introducido es mayor que el que hay que adivinar.")
    contador = contador + 1
    numero_intro = int(input("Introduzca otro numero:"))

print("Has acertado el numero, te ha llevado", contador, "intentos.")
