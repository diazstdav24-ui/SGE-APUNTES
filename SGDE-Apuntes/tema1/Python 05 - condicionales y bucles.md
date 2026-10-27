## Nivel avanzado

```Java
Switch (condicion:){

    codigo:

}
```

---

```python

point = ('2','5')
match point:
    case (x,y)


```

Usamos las tuplas para el case

---

```python
point = (	2	, 	5	)
match point:
    case (int(), int()):
        print(f	{point} is in plane	)
    case (int(), int(), int()):
        print(f	{point} is in space	)
    case _:
        print(	Unknown!	)
```

De esta forma obligamos a que mire si lo que hay en el case sion enteros, de la otra forma no tenían obligacion

---

Pythn siempre intentara asemejarse a cuendo hablamos.

Sepuede colocar un if dentro de la condición del match

- Si yo quiero romper un bucle puede usar la palabra break

- Continue permite que desde una línea se salte el final y vuelve al principio

- A los whiles en py se le puede poner un else, si ni si quiera se hace tambien salta

```python
>>> MAX_GREETS = 4
>>> num_greets = 0
>>> want_greet = 	S
>>> while want_greet == 	S	:
... print(	Hola qué tal!	)
... num_greets += 1
... if num_greets == MAX_GREETS:
... print(	Máximo número de saludos alcanzado	)
... break
... want_greet = input(	¿Quiere otro saludo? [S/N] 	)
... else:
... print(	Usted no quiere más saludos	)
... print(	Que tenga un buen día	)

```

## Bucles for:

Se usa in en lugar de : para el for each

```python

for letter in word:
    print(letter)


```

Para forzar a que el bucle paré podemos usar el break

El break es una ruptura inesperada del programa, es extraordinario. Lo mejor sería intentar salir del bucle usando condicionales

```python

for letter in word:
    if letter == 't':
        break
    print(letter)

```

Los bucles for permiten usar la función range(). Nos permite coger un rango de números para hacer una lista rapida de números

```python

for i in range(2, 10):
    print(i)

```

En los parantesis del range tiene los siguientes parametros range(start, stop,
step) :

• start: Es opcional y tiene valor por defecto 0.
• stop: es obligatorio (siempre se llega a 1 menos que este valor).
• step: es opcional y tiene valor por defecto 1.

Si no colocas nada por defecto es nulo

\_: Significa que ni si quiere tiene que usar la variable
