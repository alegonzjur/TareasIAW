# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 12:11:05 2023

@author: agonjur
"""

introducir = True
lista = []
while introducir == True:
    palabra = str(input("Introduzca una palabra:"))
    lista.append(palabra)
    introducir = input("¿Quiere seguir introduciendo palabras?") == "Si"
entero = int(input("Introduzca un numero entero:"))
for palabra in lista:
    if len(palabra) >= entero:
        print("La palabra", palabra, "tiene más de ", entero, "caracteres.")
        