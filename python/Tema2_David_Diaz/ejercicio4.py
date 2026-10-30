'''
Escriba un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un 
número y luego solicitar ese número de palabras para crear la lista. Por último, el programa tiene que escribir 
la lista.
'''


cantidad = int(input('¿Cuantas palabras caben en la lista? \n'))

palabras = []

cont = 1

while len(palabras) < cantidad:

    palabras.append(input(f'Diga la { len(palabras)+1 } palabra: '))

   

for palabra in palabras: 

    print(palabra)


'''
Forma phytonizada
'''

cantidad = int(input('¿Cuántas palabras caben en la lista? \n'))

palabras = []

for i in range(1, cantidad + 1):
    palabras.append(input(f'Diga la palabra {i}: '))

print('\n'.join(palabras))

'''
List comprehension
'''

palabras = [input(f'Diga la palabra {i}: ') for i in range(1, cantidad + 1)]