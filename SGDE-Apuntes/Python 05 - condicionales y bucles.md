# Nivel avanzado

Java
```
Switch (condicion:){

    codigo:

}
````
---
Python
```

point = ('2','5')
match point: 
    case (x,y)


```

Usamos las tuplas para el case
--- 

```
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