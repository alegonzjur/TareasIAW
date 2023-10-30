# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 12:07:33 2023

@author: agonjur
"""

introducir = True
lista = []
while introducir == True:
    palabra = str(input("Introduzca una palabra:"))
    lista.append(palabra)
    introducir = input("¿Quiere seguir introduciendo palabras?") == "Si"

print("La palabra más larga de la lista es", max(lista))