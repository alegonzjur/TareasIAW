# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 12:02:31 2023

@author: agonjur
"""

from flask import Flask, request, render_template

app = Flask(__name__)
@app.route('/', methods=['POST','GET'])

def imc():
    peso = request.form.get("peso")
    altura = request.form.get("altura")
    cal = peso/altura
    print(peso, " ",  altura, " ", cal)
    return render_template("index_1.html", peso=peso, altura=altura)
app.run()

'''    if imc < 18.5:
        print("Tu IMC es de bajo peso:", imc, 'kg.')
    elif 18.5<imc<24.9:
        print("Tu IMC es normal:", imc, 'kg.')
    elif 25<imc<29.9:
        print("Tu IMC es de sobrepeso:", imc, 'kg.')
    else:
        print("Tu IMC es de obesidad:", imc, 'kg.')'''