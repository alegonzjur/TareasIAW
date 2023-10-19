# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 10:30:23 2023

@author: agonjur
"""

#----Ejercicio 4----

f = (input("Introduzca una fecha: (formato dd/mm/aaaa):"))
f = f.split('/')
meses = {1:'Enero',2:'Febrero',3:'Marzo',4:'Abril',5:'Mayo',6:'Junio',7:'Julio',
         8:'Agosto',9:'Septiembre',10:'Octubre',11:'Noviembre',12:'Diciembre'}

print(f[0],'de',meses[int(f[1])],'del', f[2])