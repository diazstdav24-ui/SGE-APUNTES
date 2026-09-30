
continuar = 'y'
numeros = []

while continuar == 'y':
    numeros.append(int(input('Diga el primer número: ')))
    continuar = input('¿Desea continuar?y/n: ')

for palabra in numeros:
    print(palabra)
