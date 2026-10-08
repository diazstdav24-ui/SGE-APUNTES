"""

Escribe un programa que genere un número aleatorio entre 0 y 10 y
nos pida adivinarlo Tenemos 3 intentos. Puedes mirar el tutorial inicial
de Python que usamos para instalar VS Code e instalar la biblioteca numpy.

"""
from numpy import random as rnd

rng = rnd.default_rng()

rnd_number = rng.integers(0,10,10)

response = int(input("Intente adivinar el número aleatorio"))

while rnd_number != response and :
    
    print
