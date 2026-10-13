"""

Escribe un programa que genere un número aleatorio entre 0 y 10 y
nos pida adivinarlo Tenemos 3 intentos. Puedes mirar el tutorial inicial
de Python que usamos para instalar VS Code e instalar la biblioteca numpy.

"""
import numpy as np

numero_secreto = np.random.randint(0, 11)
intentos = 3

for intento in range(1, intentos + 1):
    apuesta = int(input(f"Intento {intento}/{intentos}. Adivina el número (0-10): "))

    if apuesta == numero_secreto:
        print("¡Correcto! Has ganado.")
        break
    elif apuesta < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")
else:
    print(f"Has perdido. El número era {numero_secreto}.")