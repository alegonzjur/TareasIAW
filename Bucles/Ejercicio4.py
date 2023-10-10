# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 10:33:53 2023

@author: agonjur
"""

#----Ejercicio 4----

num_intro = int(input("Introduzca un numero entero positivo:"))
lista = []

while num_intro >= 0:
    lista.append(num_intro)
    num_intro = num_intro - 1

print(lista)

#----Otra forma----

num = int(input("Introduzca otro numero positivo."))
print(list(range(num,0,-1))12)