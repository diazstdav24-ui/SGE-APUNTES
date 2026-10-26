# ============================================================
#  LISTAS EN PYTHON - Ejemplos con su print de prueba
#  Referencia: Aprende Python 2023, capítulo 5.1 (Listas)
# ============================================================

# ------------------------------------------------------------
# CREAR LISTAS
# ------------------------------------------------------------

# Lista vacia
empty_list = []
print("Lista vacia:", empty_list)

# Otra forma
empty_list2 = list()
print("Lista vacia con list():", empty_list2)

# Lista con cosas
languages = ['Python', 'Ruby', 'Javascript']
print("Lista con cosas:", languages)

# Listas anidadas (pueden mezclar tipos de datos distintos)
data = ['Tenerife', {'cielo': 'limpio', 'temp': 24}, 3718, (28.2933947, -16.5226597)]
print("Lista con tipos mezclados:", data)

# Lista de numeros
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13]
print("Lista de numeros:", fibonacci)

# ------------------------------------------------------------
# CONVERSION
# ------------------------------------------------------------

# Para convertir otros tipos de datos en una lista podemos usar la función list():
# conversión desde una cadena de texto
print("list('Python'):", list('Python'))

# Para convertir una lista explicita con los valores que constituyen el rango [0,9]
print("list(range(10)):", list(range(10)))

# ------------------------------------------------------------
# OPERACIONES CON LISTAS
# ------------------------------------------------------------

# Obtener un elemento
# Igual que en el caso de las cadenas de texto, podemos obtener un elemento de una lista
# a través del índice (lugar) que ocupa.

# Esto debería de devolver 'Python'
print("languages[0]:", languages[0])

# Acceso con índice negativo (-1 es el último)
print("languages[-1]:", languages[-1])

# Si el índice se sale de los límites, Python lanza un IndexError.
# Usamos try/except para que el programa no se pare y poder probarlo.
try:
    print(languages[3])
except IndexError as error:
    print("Error al acceder a languages[3]:", error)

# Trocear una lista
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']

# Aqui por ejemplo obtendríamos los elementos 0, 1 y 2, ya que py excluye el 3
print("shopping[0:3]:", shopping[0:3])

# Si omitimos el inicio, empieza desde el principio
print("shopping[:3]:", shopping[:3])

# Del elemento 2 al 3 (el 4 se excluye)
print("shopping[2:4]:", shopping[2:4])

# Troceado con step negativo
print("shopping[-1:-4:-1]:", shopping[-1:-4:-1])

# En el troceado NO da error si nos pasamos de rango, Python lo ajusta
print("shopping[10:]:", shopping[10:])
print("shopping[-100:2]:", shopping[-100:2])
print("shopping[2:100]:", shopping[2:100])

# Invertir una lista
# Equivale a invertir la lista (conserva la original)
print("shopping[::-1]:", shopping[::-1])

# reversed() -> Conserva la lista original
print("list(reversed(shopping)):", list(reversed(shopping)))
print("La original sigue igual:", shopping)

# Modificando la lista original:
shopping.reverse()
print("Tras shopping.reverse():", shopping)

# Añadir al final de una lista:
languages.append('Java')
print("Tras append('Java'):", languages)

# Creando desde vacío (patrón creación): números pares del [0, 20)
even_numbers = []
for i in range(20):
    if i % 2 == 0:
        even_numbers.append(i)
print("Pares del 0 al 19:", even_numbers)

# Añadir en cualquier posición de una lista con insert(indice, elemento)
shopping = ['Agua', 'Huevos', 'Aceite']
shopping.insert(1, 'Jamón')
print("insert(1, 'Jamón'):", shopping)
shopping.insert(3, 'Queso')
print("insert(3, 'Queso'):", shopping)

# insert() con índices fuera de rango no da error: se ajusta al principio o al final
shopping = ['Agua', 'Huevos', 'Aceite']
shopping.insert(100, 'Mermelada')
print("insert(100, 'Mermelada'):", shopping)
shopping.insert(-100, 'Arroz')
print("insert(-100, 'Arroz'):", shopping)

# Repetir elementos con el operador *
shopping = ['Agua', 'Huevos', 'Aceite']
print("shopping * 3:", shopping * 3)

# Combinar listas
# Conservando la lista original: operador +
fruitshop = ['Naranja', 'Manzana', 'Piña']
print("shopping + fruitshop:", shopping + fruitshop)
print("shopping no ha cambiado:", shopping)

# Modificando la lista original: extend()
shopping.extend(fruitshop)
print("Tras extend(fruitshop):", shopping)

# Cuidado: extend() con una cadena la recorre letra a letra
shopping = ['Agua', 'Huevos', 'Aceite']
shopping.extend('Limón')
print("extend('Limón'):", shopping)

# Cuidado: append() con una lista la añade como SUBLISTA
shopping = ['Agua', 'Huevos', 'Aceite']
shopping.append(fruitshop)
print("append(fruitshop):", shopping)

# Modificar un elemento a través de su índice
shopping = ['Agua', 'Huevos', 'Aceite']
shopping[0] = 'Jugo'
print("shopping[0] = 'Jugo':", shopping)

# Modificar un índice que no existe da error
try:
    shopping[100] = 'Chocolate'
except IndexError as error:
    print("Error al modificar shopping[100]:", error)

# Modificar con troceado (la lista nueva puede tener distinta longitud)
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
shopping[1:4] = ['Atún', 'Pasta']
print("shopping[1:4] = ['Atún', 'Pasta']:", shopping)

# ------------------------------------------------------------
# BORRAR ELEMENTOS
# ------------------------------------------------------------

# Por su índice: sentencia del
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
del shopping[3]
print("del shopping[3]:", shopping)

# Por su valor: remove() (si hay duplicados, solo borra la primera ocurrencia)
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
shopping.remove('Sal')
print("remove('Sal'):", shopping)

# Por su índice y recuperando el elemento: pop()
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
product = shopping.pop()          # igual que pop(-1)
print("pop() ha devuelto:", product, "| lista:", shopping)
product = shopping.pop(2)
print("pop(2) ha devuelto:", product, "| lista:", shopping)

# Por su rango: troceado asignando una lista vacía
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
shopping[1:4] = []
print("shopping[1:4] = []:", shopping)

# Borrado completo con clear() (misma zona de memoria)
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
shopping.clear()
print("Tras clear():", shopping)

# Borrado completo reinicializando con [] (nueva zona de memoria)
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
shopping = []
print("Tras shopping = []:", shopping)

# ------------------------------------------------------------
# BUSCAR
# ------------------------------------------------------------

# Encontrar el índice de un elemento con index()
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
print("index('Huevos'):", shopping.index('Huevos'))

# Si no existe, da ValueError
try:
    shopping.index('Pollo')
except ValueError as error:
    print("Error con index('Pollo'):", error)

# Pertenencia con el operador in (devuelve True o False)
print("'Aceite' in shopping:", 'Aceite' in shopping)
print("'Pollo' in shopping:", 'Pollo' in shopping)

# Número de ocurrencias con count()
sheldon_greeting = ['Penny', 'Penny', 'Penny']
print("count('Howard'):", sheldon_greeting.count('Howard'))
print("count('Penny'):", sheldon_greeting.count('Penny'))

# ------------------------------------------------------------
# LISTA <-> CADENA DE TEXTO
# ------------------------------------------------------------

# join(): une los elementos con un separador (solo funciona con cadenas)
print("', '.join:", ', '.join(shopping))
print("' '.join:", ' '.join(shopping))
print("'|'.join:", '|'.join(shopping))

try:
    print(','.join([1, 2, 3, 4, 5]))
except TypeError as error:
    print("Error con join de numeros:", error)

# ------------------------------------------------------------
# ORDENAR
# ------------------------------------------------------------

# sorted() -> conserva la lista original, devuelve una nueva
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
print("sorted(shopping):", sorted(shopping))
print("La original sigue igual:", shopping)

# sort() -> modifica la lista original
shopping.sort()
print("Tras shopping.sort():", shopping)

# Orden inverso con reverse=True
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
print("sorted(reverse=True):", sorted(shopping, reverse=True))

# ------------------------------------------------------------
# LONGITUD E ITERACION
# ------------------------------------------------------------

# Longitud con len()
print("len(shopping):", len(shopping))

# Iterar sobre una lista con for
for product in shopping:
    print("Producto:", product)

# Iterar con índice usando enumerate()
for i, product in enumerate(shopping):
    print(i, product)

# enumerate() con start para empezar a contar desde otro número
for i, product in enumerate(shopping, start=1):
    print(i, product)

# Iterar sobre varias listas a la vez con zip()
shopping = ['Agua', 'Aceite', 'Arroz']
details = ['mineral natural', 'de oliva virgen', 'basmati']
for product, detail in zip(shopping, details):
    print(product, detail)

# zip() devuelve un iterador, para verlo como lista usamos list()
print("list(zip(...)):", list(zip(shopping, details)))

# ------------------------------------------------------------
# COMPARAR LISTAS
# ------------------------------------------------------------

# Se comparan elemento a elemento: 1 == 1, 2 == 2, 3 < 4 -> True
print("[1, 2, 3] < [1, 2, 4]:", [1, 2, 3] < [1, 2, 4])

# ------------------------------------------------------------
# CUIDADO CON LAS COPIAS
# ------------------------------------------------------------

# Asignación simple: las dos variables apuntan a la MISMA lista
original_list = [4, 3, 7, 1]
copy_list = original_list
original_list[0] = 15
print("original:", original_list, "| 'copia':", copy_list)

# Copia real con copy()
original_list = [4, 3, 7, 1]
copy_list = original_list.copy()
original_list[0] = 15
print("original:", original_list, "| copy():", copy_list)

# Copia real con troceado completo [:]
original_list = [4, 3, 7, 1]
copy_list = original_list[:]
print("¿Son objetos distintos?:", id(original_list) != id(copy_list))

# Si la lista contiene elementos mutables hace falta deepcopy()
from copy import deepcopy
original_list = [[1, 2], [3, 4]]
copy_list = deepcopy(original_list)
original_list[0][0] = 99
print("original:", original_list, "| deepcopy():", copy_list)

# ------------------------------------------------------------
# VERACIDAD MULTIPLE: all() y any()
# ------------------------------------------------------------

# all(): True solo si se cumplen TODAS las condiciones
word = 'python'
enough_length = len(word) > 4
right_beginning = word.startswith('p')
min_ys = word.count('y') >= 1
print("all([...]):", all([enough_length, right_beginning, min_ys]))

# any(): True si se cumple ALGUNA condición
word = 'yeah'
enough_length = len(word) > 4
right_beginning = word.startswith('p')
min_ys = word.count('y') >= 1
print("any([...]):", any([enough_length, right_beginning, min_ys]))
