# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 10:29:18 2023

@author: agonjur
"""

#↕----Ejercicio 3----

num_intro = int(input("Introduzca un numero entero positivo:"))
contador = 1
lista = []
while contador <= num_intro:
    lista.append(contador)
    contador = contador + 2

print(lista)
    