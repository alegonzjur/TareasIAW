# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 10:46:53 2023

@author: agonjur
"""

#----Ejercicio 5----

asignaturas =  {'Matemáticas': 6, 'Física': 4, 'Química': 5}
contador = 0

for nombre,creditos in asignaturas.items():
    print(nombre,'tiene',creditos,'creditos.')
    contador += creditos

print("El numero total de creditos es", contador)