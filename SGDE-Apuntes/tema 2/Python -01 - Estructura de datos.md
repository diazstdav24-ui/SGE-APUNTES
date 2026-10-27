ºbgn

# Estructuras de datos

En las estructuras de datos son mutables, es decir se pueden modificar, añadir y borrar

Se pueden crear listas vacías, son dinamicas como las colecciones en Java.

Las listas permiten meter elemntos de cualquier tipo, incluso se pueden anidar listas.

La mejor forma de crear una lista vacia es con los corchetes

Para sacar un elemento = `lista[0]`

Empieza en el 0 y llega a uno menos, osea que empieza en el cero y termina en el dos `shopping[0:3]`

Poner la lista al reves conservando la lista original:

`shopping[::-1]` o `list(reversed(shopping))`

Modificando la lista original:

`shopping.reverse()` sin la "d" al final

`shopping.insert(1,  Jamón )` sirve para inserta la posición exacta que deseamos insertar, modifica la lista original

- Combinar listas, se puede hacer de dos formas:

1. modificnado la original:

shopinng + fruitshop
ºe

2. conservando la original

shoppig.extend(fruitshop)
ºe

`En este caso hay que tener cuidado debido a que si le pasamos a extend una palabra puede pasar esto`

`[ Agua ,  Huevos ,  Aceite ,  L ,  i ,  m ,  ó ,  n ]`

Troceado puede ser que caiga en clase, por ejemplo aqui `shopping[1:4] = []`

ºend
