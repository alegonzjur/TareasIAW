# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 12:00:33 2023

@author: agonjur
"""

#----Ejercicio 8----

frase = str(input("Introduzca una frase:"))
letra = str(input("Introduzca una letra:"))
contador = 0

for i in frase:
    if i == letra:
        contador += 1
print("La letra", letra,"aparece", contador, "veces en la frase.")