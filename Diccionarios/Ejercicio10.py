# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 18:37:21 2023

@author: agonjur
"""

#----Ejercicio 10----
dicc = dict()
clave = str()
dicc_aux = {"nombre","direccion","telefono","correo","preferente"}
dicc[clave] = dicc_aux
opcion = ' '
while opcion != 6:
    if opcion == 1:
        clave = input("Introduzca su NIF:")
        datos = input("Introduzca sus datos:(,)")
        datos.split(',')
        dicc.aux[datos]
        dicc[clave] += dicc.aux
    if opcion == 2:
        NIF = input("Introduzca su NIF:")
        if NIF in dicc:
            dicc.pop(NIF)
    if opcion == 3:
        NIF = input("Introduzca su NIF:")
        if NIF in dicc:           
            print("El NIF es:",NIF)
            for clave, valor in dicc.items():
                print(clave, ':',valor)
        else:
            print("No existen datos sobre es NIF.")    
    if opcion == 4:
        for clave,valor in dicc.items():
            print(clave, ':', valor['nombre'])
    if opcion == 5:
        for clave, valor in dicc.items():
            if valor['preferente'] == True:
                print(clave, ':', valor['nombre'])
opcion = input('Menú de opciones\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar clientes\n(5) Listar clientes preferentes\n(6) Terminar\nElige una opción:')