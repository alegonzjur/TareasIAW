# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 12:01:09 2023

@author: agonjur
"""

#Ejercicio 4

num_alumnos = int(input("Introduzca el numero de alumnos a almacenar:"))
contador = 0
dicc = dict()
while contador < num_alumnos:
    nombre = str(input("Introduzca el nombre del alumno:"))
    introducir = True
    lista = []
    while introducir == True:
        nota = int(input("Introduzca una nota:"))
        if nota > 0:
            lista.append(nota)
            introducir = True
        if nota < 0:
            lista.append(nota)
            introducir = False
        dicc[nombre] = lista
    contador += 1

for x,y in dicc.items():
    print("El alumno", x, "ha tenido una nota media de", sum(y)/len(y))