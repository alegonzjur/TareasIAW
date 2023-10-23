# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 12:00:09 2023

@author: agonjur
"""

#----Ejercicio 8----
dicc = dict()
palabras = str(input("Introduce las palabras en este formato: palabra:traduccion, palabra1:traduccion1"))
for i in palabras.split(','):
    esp, ing = i.split(':')
    dicc[esp] = ing
    
frase = input("Introduzca su frase en español.")
for i in frase.split():
        if i in dicc:
            print(dicc[i], end=' ')
        else:
            print(i, end=' ')
