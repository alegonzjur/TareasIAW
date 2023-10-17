# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 12:24:39 2023

@author: agonjur
"""

#---Ejercicio 9----

palabra = str(input("Introduzca una palabra:"))
lista = []
for i in palabra:
    lista.append(i)
print(lista[::-1])

