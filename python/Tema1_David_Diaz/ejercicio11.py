objetivo = int(input("Diga el primer número: "))
numeros = []
suma = 0

while suma != objetivo:
    n = int(input("Siguiente número: "))
    numeros.append(n)
    suma += n

print(f"La suma es igual que {objetivo}")
print(numeros)