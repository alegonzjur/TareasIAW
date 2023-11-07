# -*- coding: utf-8 -*-

#Ejercicio 2 de Bucles
'''
try:
    edad = int(input("Introduzca su edad:"))
    for i in range(edad):
        print("Has cumplido", str(i+1), "años.")
except ValueError:
    print("Trataste de poner un valor que no es un entero.")
'''
#Ejercicio 2 de Bucles de otra forma.
'''
while True:
    try:
        age = int(input("Introduzca su edad:"))
        for i in range(age):
            print("Has cumplido", str(i+1), "años.")
        break
    except ValueError:
        print("Tiene que introducir un número.")
        continue
'''

#Ejercicio 3
while True:
    try:
        num_intro = int(input("Introduzca un numero entero positivo:"))
        if num_intro <0:
            print("No se admiten numeros negativos.")
            continue
        contador = 1
        lista = []
        while contador <= num_intro:
            lista.append(contador)
            contador = contador + 2
        break
    except ValueError:
        num_intro = int(input("Introduzca un numero entero positivo:"))
print(lista)