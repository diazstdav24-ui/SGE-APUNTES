### ags

python,dam,apuntes,tipos-de-datos

### Aliases

Tema 3 Python,Tipos de datos en Python

### Fuente

Aprende Python (S. Delgado Quintero, 2023), cap. 3, pp. 47-100

### Creado

2026-09-24

# Tipos de datos en Python

> [!abstract] Cómo leer estos apuntes
> 
> - Texto normal → tuyo, reorganizado.
> - 🆕 → añadido (del libro o de conocimiento general).
> - 🔧 → corrección de algo que tenías en tus apuntes.
> - 🧪 → reto para que lo pruebes tú en el intérprete. Las respuestas están plegadas: intenta predecir antes de abrirlas.
> - `(p. X)` → página del libro donde profundizar.

Anterior: [[Python 01-02 - Introducción y entorno]] · Índice: [[Python 00 - Índice]]

---

## 1. Todo es un objeto (p. 48)

- Cada dato en memoria es un **objeto** con, al menos, tres campos: **tipo**, **identificador único** (`id()`) y **valor**.
- 🆕 Por eso se dice que "en Python todo es un objeto", incluidos `int`, `bool` o `float`. No existen tipos primitivos como en Java.

|Tipo|Nombre|Literal de ejemplo|¿Mutable?|
|---|---|---|---|
|`bool`|Booleano|`True`, `False`|No|
|`int`|Entero|`21`, `34_500`|No|
|`float`|Flotante|`3.14`, `1.5e3`|No|
|`complex` 🆕|Complejo|`2j`, `3 + 5j`|No|
|`str`|Cadena|`'tfn'`|No|
|`tuple`|Tupla|`(1, 3, 5)`|No|
|`list`|Lista|`['Chrome', 'Firefox']`|**Sí**|
|`set`|Conjunto|`{2, 4, 6}`|**Sí**|
|`dict`|Diccionario|`{'Chrome': 'v79'}`|**Sí**|

## 2. Variables (p. 50)

Una variable es un **nombre** que apunta a un objeto en memoria.

**Reglas obligatorias**

1. Solo letras (mayúsculas o minúsculas), dígitos y guion bajo `_`.
2. Empieza por letra o `_`, **nunca** por dígito.
3. No puede ser una palabra reservada (`for`, `if`, `class`, `None`, `True`...). Lista completa con `help('keywords')`.
4. Distingue mayúsculas de minúsculas (_case-sensitive_): `stuff` y `Stuff` son variables distintas.

**Convenciones (PEP 8)**

- Variables y funciones en `snake_case`: `num_songs`.
- Constantes en `MAYÚSCULAS`: `LIGHT_SPEED`.
- Nombres autoexplicativos, buscando equilibrio: ni `n` (muy corto) ni `number_of_elements_to_be_handled` (muy largo).
- Variables → sustantivos, funciones → verbos, booleanos → adjetivos o preguntas (`available`, `is_opened`).
- Se recomienda el inglés para los nombres, para que cualquiera pueda leer el código.

> [!warning] 🆕 Las constantes en Python no existen de verdad Escribir en mayúsculas es solo un **acuerdo entre programadores**. Nada impide reasignar `LIGHT_SPEED`. En Java `final` te lo impide; aquí no. Y no confundas constante con tipo inmutable (ver [[#5. Mutabilidad]]).

> [!question]- 🧪 ¿Por qué fallan `7floor = 40`, `for = 3` y `screen-size = 14`? Empieza por un dígito; es una palabra reservada; el guion no es un carácter permitido (Python lo interpreta como una resta).

---

## 3. Asignación (p. 53)

- `=` **no es igualdad matemática**: es una sentencia que asigna el valor de la derecha al nombre de la izquierda.
- La variable que uses a la derecha tiene que existir ya, si no da `NameError`.

**Asignación múltiple** (tus apuntes)

python

```python
#Asignación multiple
tres = three = dre = 3

x,y,z = 10, 20, 30
```

🆕 Son **dos cosas distintas**:

- La primera línea es una asignación **encadenada**: los tres nombres reciben el mismo valor (`3`).
- La segunda es un **desempaquetado**: cada nombre recibe el valor que ocupa su misma posición. Si el número de nombres y de valores no coincide, salta un `ValueError`.

> [!question]- 🧪 Intercambiar dos variables sin usar una variable auxiliar En Java necesitas una variable temporal. En Python hay una forma directa que usa justo el desempaquetado. Intenta deducirla tú a partir de lo de arriba y pruébala en el intérprete.

**Comprobar valor y tipo**

- En el intérprete basta con escribir el nombre. En un script hay que usar `print()`.
- `type(x)` devuelve el tipo. 🆕 `isinstance(x, int)` responde `True` o `False` y es la forma preferida cuando haces una comprobación en el código (p. 70).

---

## 4. Las variables son nombres, no cajas (p. 56)

> [!bug] 🔧 Corrección de tus apuntes Tenías este texto bajo el título "Conversión implícita", pero **habla de memoria y referencias, no de conversión**. Lo he movido aquí. La conversión implícita real está en [[#9. Conversión de tipos]]. Además, la frase _"la variable apunta a la dirección de memoria y es la dirección la que apunta al objeto"_ es circular. Lo correcto: **nombre → referencia → objeto** (que lleva su tipo, su `id` y su valor).

**Comparación con Java** 🆕

||Java|Python|
|---|---|---|
|Tipos primitivos (`int`, `boolean`...)|La variable guarda el valor directamente|No existen: todo es objeto|
|Objetos|La variable guarda una referencia|Igual, y **siempre**|
|¿Quién tiene el tipo?|La variable (tipado estático)|**El objeto**; el nombre puede apuntar luego a otro de distinto tipo|

**Consecuencias**

- `b = a` **no copia** el objeto: `a` y `b` apuntan al mismo objeto (`id(a) == id(b)`).
- Reasignar (`a = 7`) hace que `a` apunte a **otro** objeto. `b` sigue apuntando al original.
- 🆕 `is` compara **identidad** (¿es el mismo objeto?), mientras que `==` compara **valor** (¿son iguales?).

> [!tip] Herramienta Python Tutor (pythontutor.com) dibuja paso a paso a qué apunta cada nombre. El libro enlaza un ejemplo: [https://cutt.ly/lvCyXeL](https://cutt.ly/lvCyXeL)

---

## 5. Mutabilidad (p. 58)

- **Mutable**: se puede modificar el contenido del objeto en su misma zona de memoria.
- **Inmutable**: no se puede modificar in-situ. Solo se puede hacer que el nombre apunte a otro objeto.

|Inmutables|Mutables|
|---|---|
|`bool`, `int`, `float`, `str`, `tuple`|`list`, `set`, `dict`|

> [!note] Importante (tus apuntes) Que un tipo sea inmutable significa que no puedes modificar su valor in-situ, pero **siempre** puedes asignarle un valor nuevo (hacerlo apuntar a otra zona de memoria).

🆕 Matices que te van a salvar de bugs:

- Una **tupla** es inmutable, pero si contiene una lista, **esa lista sí se puede modificar**. La inmutabilidad es de la tupla, no de lo que guarda dentro.
- **Aliasing**: si haces `b = a` con una lista y modificas `b`, verás el cambio también en `a`, porque son el mismo objeto. Es el error clásico del capítulo 5.
- `str` es inmutable: los métodos como `upper()` o `strip()` **devuelven una cadena nueva**, no modifican la original.

> [!question]- 🧪 Si `a = 5` y `b = a`, y luego haces `a = 7`, ¿cuánto vale `b`? ¿Y si fueran listas y modificas el contenido de `a`? Con enteros, `b` sigue valiendo 5 (`a` apunta a otro objeto). Con listas y una modificación del contenido, `b` cambia también (mismo objeto, contenido modificado). Compruébalo con `id()` y con Python Tutor.

---

## 6. Booleanos (p. 60)

- Solo dos valores: `True` y `False`, **con la primera letra en mayúscula**. Escribir `true` da `NameError`.
- Numéricamente, `True` equivale a `1` y `False` a `0`.
- 🔧 En tus apuntes ponía _"los booleanos sí pueden devolver 1 o 0"_. Más preciso: **`bool` es una subclase de `int`**, así que un booleano _es_ un entero con dos valores posibles. Por eso se pueden sumar y multiplicar.
- Convención: nombrar las variables booleanas como pregunta o adjetivo (`is_opened`, `has_sugar`).

---

## 7. Enteros (p. 62)

- Literales: pueden llevar signo. **No pueden empezar por 0** (`08` es un `SyntaxError`). Se pueden separar con guiones bajos para leer mejor (`3_000_000`).
- 🆕 **Tamaño ilimitado**: no hay _integer overflow_ como en `int`/`long` de Java. Solo está limitada la memoria (p. 67).

**Operadores**

|Operador|Qué hace|Ejemplo|Resultado|
|---|---|---|---|
|`+`|Suma|`3 + 9`|`12`|
|`-`|Resta|`6 - 2`|`4`|
|`*`|Multiplicación|`5 * 5`|`25`|
|`/`|División (🆕 **siempre devuelve `float`**)|`9 / 2`|`4.5`|
|`//`|División entera|`9 // 2`|`4`|
|`%`|Módulo (resto)|`9 % 4`|`1`|
|`**`|Exponenciación|`2 ** 4`|`16`|

> [!note] Sobre el `2 ** 4` suelto de tus apuntes Estaba junto a la frase de los booleanos, pero no tiene relación con ella: es el operador de exponenciación. Lo he movido a esta tabla. Además, elevar a `0.5` equivale a la raíz cuadrada.

**Prioridad (de mayor a menor)**: `()` → `**` → `-a` / `+a` → `*` `/` `//` `%` → `+` `-`

**Asignación aumentada**: `+=`, `-=`, `*=`, `//=`, `**=`... hacen la operación y asignan en un paso.

- 🆕 **Python no tiene `++` ni `--`**. Se usa `+= 1`. Es un error habitual viniendo de Java.

**Otros**

- Dividir entre 0 → `ZeroDivisionError`.
- `abs()` da el valor absoluto.
- Buen estilo: un espacio a cada lado de los operadores.

> [!question]- 🧪 ¿Qué devuelven `-7 // 2` y `-7 % 2`? ¿Coincide con lo que haría Java? `-7 // 2` da `-4` (la división entera **redondea hacia abajo**, no hacia cero) y `-7 % 2` da `1` (el resto toma el signo del divisor). En Java, `-7 / 2` da `-3` y `-7 % 2` da `-1`. Es una diferencia real entre los dos lenguajes.

---

## 8. Flotantes (p. 67)

- Números con parte decimal. Formas equivalentes de escribir `4.0`: `4.0`, `4.`, `4e0`. Notación científica: `1.5e3`.
- 🆕 Un `float` de Python equivale al `double` de Java (64 bits).
- A diferencia de los enteros, **tienen límites** (máximo aproximado 1.8e308, en `sys.float_info`).

**Errores de aproximación** (p. 70)

- Usan el estándar IEEE 754 con aritmética finita, así que `(19 / 155) * (155 / 19)` da `0.9999999999999999` y no `1.0`.
- Solución sencilla: `round(x, n)` para redondear a `n` decimales.
- 🆕 **Nunca compares flotantes con `==`** tras hacer cálculos. Y para dinero, lo profesional es usar el módulo `decimal`.

> [!warning] `round()` vs `int()` `round()` aproxima al más cercano. `int()` **descarta** la parte decimal. No son lo mismo. 🆕 Además, `round()` usa redondeo "al par más cercano" en los casos de `.5` justo: `round(2.5)` da `2` y `round(3.5)` da `4`.

---

## 9. Conversión de tipos (p. 68)

### Conversión implícita (promoción)

Al mezclar `bool`, `int` y `float`, Python promociona automáticamente al tipo de **mayor rango**:

|Tipo 1|Tipo 2|Resultado|
|---|---|---|
|`bool`|`int`|`int`|
|`bool`|`float`|`float`|
|`int`|`float`|`float`|

Por eso `True + 25` da `26` y `10 + 11.3` da `21.3`.

### Conversión explícita

Funciones: `bool()`, `int()`, `float()`, y `str()` para pasar a texto.

- `bool(1)` → `True`, `bool(0)` → `False`
- `int(True)` → `1`, `int(False)` → `0`
- `float(1)` → `1.0`, `float(True)` → `1.0`
- `int(3.1)`, `int(3.5)` e `int(3.9)` → `3` en los tres casos

> [!bug] 🔧 `int()` no es "la parte baja" (suelo) Tus apuntes (copiados del libro) dicen que `int(x)` equivale a ⌊x⌋. Eso solo es cierto con positivos. En realidad **`int()` trunca hacia cero**. Pruébalo con negativos: ¿qué da `int(-3.9)`? (`-3`, no `-4`). Para el suelo de verdad existe `math.floor()`.

🆕 **Verdad o falsedad de otros valores** (te hará falta en el capítulo 4 con los `if`):

- `bool()` da `False` para `0`, `0.0` y la cadena vacía `''`. Para casi todo lo demás da `True`.
- Trampa típica: `bool('False')` es `True`, porque la cadena no está vacía.

🆕 **Cadena → número**

- `int('10')` y `float('21.7')` funcionan. `int('3.5')` da `ValueError`.
- `int('FF', 16)` interpreta el texto en base 16 y da `255`. Por defecto la base es 10.
- `input()` **siempre devuelve `str`**: si vas a operar con el número, conviértelo.

---

## 10. Bases numéricas (p. 72)

|Base|Símbolos|Prefijo del literal|Función|
|---|---|---|---|
|Binaria|0-1|`0b`|`bin()`|
|Octal|0-7|`0o`|`oct()`|
|Hexadecimal|0-9, A-F|`0x`|`hex()`|

Las letras hexadecimales no distinguen mayúsculas de minúsculas. Las funciones devuelven el resultado como **cadena** con el prefijo.

---

## 11. Cadenas de texto (`str`) (p. 75)

### Crear cadenas

- 🔧 Tus apuntes decían "van entre comillas simples". Se puede con **simples `'...'`, dobles `"..."` o triples `'''...'''`**. Las triples sirven para texto multilínea.
- Usar unas dentro de las otras evita escapar: una cadena con comillas dobles dentro se escribe con simples por fuera, y viceversa. Elige un estilo y sé consistente.
- Cadena vacía: `''`.
- Python 3 usa **Unicode**, así que admite tildes, ñ y emojis sin más.

### Secuencias de escape (p. 77)

`\n` salto de línea · `\t` tabulador · `\'` comilla simple · `\\` barra invertida.

- Verás su efecto real al usar `print()`.
- **Cadenas _raw_**: con una `r` delante del literal, las barras pierden su significado especial. Se usan mucho en expresiones regulares.

### Operaciones básicas (p. 81)

- `+` concatena, `*` repite.
- Indexado: `s[0]` es el primero, `s[-1]` es el último. Fuera de rango → `IndexError`.
- **Slicing**: `[start:end:step]`. El inicio **sí** se incluye, el final **no**. Cada parte es opcional.
- `len(s)` da la longitud. `in` y `not in` comprueban pertenencia. 🆕 Se prefiere `'C' not in s` en lugar de `not('C' in s)`.
- `str` es inmutable: asignar `s[4] = 'D'` da `TypeError`.

> [!question]- 🧪 Con `s = 'Agua pasada'`, ¿qué crees que devuelven `s[:4]`, `s[5:]`, `s[::-1]` y `s[::2]`? `'Agua'`, `'pasada'`, la cadena al revés (`'adasap augA'`) y una letra sí, una no (`'Au aaa'`). Un paso negativo recorre la cadena hacia atrás; el libro no lo cubre, así que compruébalo tú.

### Métodos que debes conocer (pp. 85-90)

Todos **devuelven una cadena nueva**; ninguno modifica la original.

|Necesito...|Método|
|---|---|
|Dividir por un separador (devuelve una lista)|`split()` (por defecto, espacios en blanco)|
|Dividir en 3 partes: izquierda, separador, derecha|`partition()`|
|Quitar relleno al principio y al final|`strip()`, `lstrip()`, `rstrip()`|
|¿Empieza o termina por...?|`startswith()`, `endswith()`|
|Posición de la primera aparición|`find()` (da `-1` si no está), `index()` (da `ValueError`)|
|Contar apariciones|`count()`|
|Reemplazar (opcionalmente solo N veces)|`replace()`|
|Cambiar mayúsculas|`capitalize()`, `title()`, `upper()`, `lower()`, `swapcase()`|
|Comprobar contenido|`isalnum()`, `isalpha()`, `isnumeric()`, `isupper()`, `islower()`, `istitle()`|
|🆕 Unir una lista en una cadena (inverso de `split`)|`join()`|

### Comparar cadenas (p. 95)

- Se compara **lexicográficamente**, carácter a carácter, usando su código Unicode (`ord()`).
- Las mayúsculas van **antes** que las minúsculas (`A` = 65, `a` = 97). `chr()` hace el camino inverso.

---

## 12. Mostrar y pedir datos

**`print()`** (p. 79)

- Acepta varios argumentos separados por comas.
- `sep` cambia el separador (por defecto, un espacio). `end` cambia lo que se imprime al final (por defecto, salto de línea).

**`input()`**

- Muestra un mensaje y lee del teclado. **Siempre devuelve `str`.**
- ⚠️ Nunca llames `input` a una variable: pisarías la función.

**f-strings** (Python ≥ 3.6, p. 90): anteponer `f` a la cadena y poner las variables o expresiones entre `{}`.

- Si olvidas la `f`, no se sustituye nada.
- Para mostrar una llave literal, se duplica: `{{` y `}}`.
- Estilos antiguos (`%` y `.format`) los verás en código heredado, pero para código nuevo usa f-strings.

|Formato dentro de `{}`|Efecto|
|---|---|
|`{x:.2f}`|2 decimales|
|`{x:10d}` / `{x:010d}`|Entero con ancho 10 / rellenando con ceros|
|`{x:<7}` `{x:^7}` `{x:>7}`|Alinear a izquierda / centro / derecha|
|`{x:b}` `{x:o}` `{x:x}`|Binario / octal / hexadecimal|
|`{x:e}`|Notación científica|
|`{x=}`|Modo _debug_ (Python ≥ 3.8): imprime nombre y valor|
|`{x!r}`|Representación interna (las cadenas salen con comillas)|

## 13. Funciones _built-in_ de este tema

|Función|Para qué|
|---|---|
|`type()`, `isinstance()`|Conocer / comprobar el tipo|
|`id()`|Identidad (dirección) del objeto|
|`len()`|Longitud|
|`abs()`, `round()`|Valor absoluto, redondeo|
|`bool()`, `int()`, `float()`, `str()`|Conversiones|
|`bin()`, `oct()`, `hex()`|Cambiar de base|
|`chr()`, `ord()`|Carácter ↔ código Unicode|
|`print()`, `input()`|Salida / entrada|
|`help()`, `dir()`|Ayuda / ver qué métodos tiene un objeto|

> [!tip] `dir()` y `help()` son tu mejor amigo `dir('hola')` lista todos los métodos de `str` y `help(str.find)` te explica uno concreto. Es la forma de aprender sin depender de apuntes.

---

## 14. 🆕 Errores típicos y qué significan

|Error|Suele ser porque...|
|---|---|
|`SyntaxError`|Nombre inválido o sintaxis mal escrita|
|`NameError`|Usas una variable que no existe (o escribiste `true` en minúscula)|
|`TypeError`|Operación sobre tipos incompatibles, o intentas modificar algo inmutable|
|`ValueError`|El tipo es correcto pero el valor no (`int('abc')`)|
|`IndexError`|Índice fuera de rango|
|`ZeroDivisionError`|Dividiste entre 0|

## 15. 🧪 Retos para practicar (sin solución, a propósito)

Del libro, parafraseados. Predice el resultado **antes** de ejecutar.

1. Asigna el entero `2001` a `space_odyssey` y muéstralo.
2. Averigua el tipo de un literal de texto y el de `True`.
3. Guarda `10 * 3.0` en `result`. ¿Qué tipo esperas que tenga? Comprueba.
4. Programa que lea dos enteros y muestre el resultado de las cuatro operaciones básicas con un formato tipo `7+4=11`.
5. Dado `e = 2.71828`, consigue con f-strings salidas con 3 decimales, con 6, con ancho fijo y en notación científica (p. 94).
6. Ejercicios de repaso `pycheck` de la p. 73 (círculo, esfera, triángulo, distancia euclídea...).

Cuando los tengas, me los pasas y los revisamos juntos.

---