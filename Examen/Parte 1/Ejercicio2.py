# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 10:21:08 2023

@author: agonjur
"""

#Ejercicio 2

lista = []
introducir = True
while introducir == True:
    num = int(input("Introduzca un número:"))
    lista.append(num)
    introducir = input('¿Desea introducir más numeros?:') == 'Si'

num_buscar = int(input("Introduzca el numero a buscar:"))
contador = 0
if num_buscar in lista:
    for num_buscar in lista:
        contador += 1
else:
    print("El número no se encuentra en la lista.")
print("El numero", num_buscar, "aparece", contador,"vez/veces.")