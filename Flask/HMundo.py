# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 10:40:17 2023

@author: agonjur
"""

from flask import Flask

app = Flask(__name__)
@app.route('/')

def hola():
    return "Hola, bienvenido."

app.run()