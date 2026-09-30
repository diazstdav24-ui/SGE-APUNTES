
continuar = 'y'
palabras = []

while continuar == 'y':
    palabras.append(input('Diga la primera palabra: '))
    continuar = input('¿Desea continuar?y/n: ')

for palabra in palabras:
    print(palabra)
