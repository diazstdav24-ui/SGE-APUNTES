
import random

numero_aleatorio = random.randrange(50)

maximo = 10

if numero_aleatorio <= maximo: 
    
    print(f"El número : {numero_aleatorio}, es menor de 10")

elif 11 < numero_aleatorio < 20:
    print(f"El número está entre el 11 y el 20.Número: {numero_aleatorio} ")
    
elif 21 < numero_aleatorio < 30: 
    
    print(f"El número está entre el 21 y el 30.Número: {numero_aleatorio} ")

else: 
    print(f"El número: {numero_aleatorio}, es mayor que 30")
