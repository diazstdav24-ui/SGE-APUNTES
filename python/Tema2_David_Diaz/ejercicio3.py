"""
3. Se quiere realizar un programa que lea por teclado las distintas notas obtenidas por un alumno (comprendidas 
entre 0 y 10). A continuación, debe mostrar todas las notas a modo boletín de calificaciones, la nota media, la 
nota más alta que ha sacado, la menor y el número de suspensos. 
"""

#Mi versión(más javaniana)

count = 2
continuar = True
noteList = []
asignaturas = []
cont = 1
isValid = True
total = 0
suspensos = 0


while continuar: 


    while isValid: 

        asignatura = input(f'Diga la asignatura {cont}: ')
        nota = float(input(f"Diga la nota {cont}:"))

        if 0<= nota <= 10:

            isValid = False

            asignaturas.append(asignatura)
            noteList.append(nota)

        else: 

            isValid = True

    opcion = int(input('¿Deseas continuar? 1.Y 2.N'))

    if opcion == 1:

        isValid = True
        cont += 1 

    else: 

        continuar = False



print('Asignatura | Notas' )
for asignatura, nota in zip(asignaturas, noteList):

    print(f'{asignatura} | {nota}')


for nota in noteList: 

    total = total + nota


total /= len(noteList)

for nota in noteList: 

    if nota <= 5:


        sum(suspensos)
        

print(f"La media es de: {total}")

    
print(f'La mayor nota: {max(noteList)}')

print(f'La menor nota: {min(noteList)}')


print(f"Números de suspensos: {suspensos}")


#La de la IA en una forma mas pythonica
def pedir_nota(mensaje):
    while True:
        try:
            nota = float(input(mensaje))
        except ValueError:
            print("Introduce un número válido.")
            continue
        if 0 <= nota <= 10:
            return nota
        print("La nota debe estar entre 0 y 10.")

asignaturas = []
notas = []

while True:
    asignaturas.append(input(f"Asignatura {len(asignaturas) + 1}: "))
    notas.append(pedir_nota(f"Nota de {asignaturas[-1]}: "))
    if input("¿Otra asignatura? (s/n): ").lower() != "s":
        break

print("\nAsignatura | Nota")
for asignatura, nota in zip(asignaturas, notas):
    print(f"{asignatura} | {nota}")

print(f"\nMedia: {sum(notas) / len(notas):.2f}")
print(f"Mayor: {max(notas)}")
print(f"Menor: {min(notas)}")
print(f"Suspensos: {sum(nota < 5 for nota in notas)}")