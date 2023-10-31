# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 11:50:59 2023

@author: agonjur
"""

#Ejercicio 3

lista = []
contador = 0
while contador<5:
    nota = float(input("Introduzca una nota:"))
    lista.append(nota)
    contador += 1
print('Las notas del alumno son', lista)
print('La nota más alta es', max(lista))
print('La nota más baja es', min(lista))
print('La nota media es', sum(lista)/len(lista))