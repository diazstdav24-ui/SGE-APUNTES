### Tags

python,dam,apuntes,introduccion,entorno

### Aliases

Intro Python,Entorno de desarrollo Python

### Fuente

Aprende Python (S. Delgado Quintero, 2023), caps. 1-2, pp. 3-46

### Creado

2026-09-24

# Introducción y entorno de desarrollo

> [!info] Nota Tus apuntes no cubrían estos capítulos, así que **todo lo de esta nota es 🆕 añadido**, resumido de lo esencial. Si ya tienes apuntes de esta parte en otro sitio, dímelo y los fusiono.

Índice: [[Python 00 - Índice]] · Siguiente: [[Python 03 - Tipos de datos]]

---

## 1. Qué es Python (cap. 1, p. 13)

- Lenguaje **interpretado**, **multiplataforma**, de **propósito general** y **multiparadigma** (imperativo, orientado a objetos y, en menor medida, funcional).
- Su filosofía prioriza un **código legible**, casi como pseudocódigo.

### Tipado: dinámico y fuerte

- **Dinámico**: una variable puede apuntar a objetos de distinto tipo a lo largo del programa. El tipo lo tiene el objeto, no el nombre.
- **Fuerte**: no puedes operar con tipos distintos sin conversión explícita (con la excepción de la promoción numérica `bool` → `int` → `float`, ver [[Python 03 - Tipos de datos#9. Conversión de tipos]]).
- No lo confundas: JavaScript es dinámico y **débil**, Java es estático y fuerte.

### Python frente a Java (para tu contexto de 2DAM)

|Aspecto|Python|Java|
|---|---|---|
|Ejecución|Interpretado (CPython compila internamente a bytecode y lo ejecuta su máquina virtual)|Compilado a bytecode y ejecutado en la JVM|
|Tipado|Dinámico, fuerte|Estático, fuerte|
|Bloques de código|**Indentación**|Llaves `{}`|
|Fin de sentencia|Salto de línea|`;`|
|Tipos primitivos|No existen (todo es objeto)|Sí (`int`, `boolean`...)|

### Ventajas y desventajas

- **A favor**: libre y gratuito, fácil de leer y aprender, muy productivo, librerías muy extensas, gran comunidad.
- **En contra**: menor velocidad de ejecución, mayor consumo de memoria, los errores de tipo no se detectan al compilar (saltan al ejecutar), débil en desarrollo móvil.

---

## 2. Versiones e implementaciones (pp. 17-19)

- **Usa siempre Python 3.** El soporte oficial de Python 2.7 terminó el 1 de enero de 2020 y el código de Python 2 no es compatible directamente con 3.
- Cuando dices "Python" te refieres (casi siempre) a **CPython**, la implementación de referencia, escrita en C. Existen otras (Jython sobre Java, IronPython sobre C#, MicroPython para microcontroladores...).
- Algunas funciones dependen de la versión (p. ej. los f-strings exigen ≥ 3.6 y su modo _debug_ ≥ 3.8), así que ten presente qué versión tienes.

---

## 3. Zen de Python y buenas prácticas (pp. 19-22)

- Ejecutando `import this` en el intérprete aparece el **Zen de Python** (Tim Peters), un conjunto de principios. Los que más te conviene interiorizar: lo explícito es mejor que lo implícito, lo simple es mejor que lo complejo y la legibilidad cuenta.
- **PEP 8** es la guía oficial de estilo (nombres, espacios, longitud de línea). Aplícala desde el principio: es lo que se espera en cualquier equipo.
- Los PEP (_Python Enhancement Proposals_) son las propuestas de mejora del lenguaje.

---

## 4. Entorno de desarrollo (cap. 2)

### Para empezar: Thonny (p. 24)

Editor sencillo con intérprete y **depurador** paso a paso integrados. Ideal para aprender a ver qué hace cada línea.

### En un entorno real (p. 28)

- **`pip`** es el gestor de paquetes. Instala, desinstala y actualiza paquetes desde **PyPI**, el repositorio oficial. (Con Anaconda se usa `conda`.)
- **Entornos virtuales**: cada proyecto necesita sus propios paquetes y a veces otra versión de Python. Un entorno virtual aísla las dependencias de cada proyecto para que no se pisen entre sí.
    - La forma más sencilla es el módulo `venv` de la librería estándar, que crea una carpeta (`.venv`) que luego **se activa**. Los comandos exactos están en la p. 30 del libro.
    - Otras herramientas: `virtualenv` / `virtualenvwrapper` (facilitan gestionar entornos) y `pyenv` (cambiar entre versiones de Python sin tocar el sistema).
- 🆕 Buenas costumbres: **no** subir la carpeta `.venv` a Git (va en `.gitignore`) y guardar las dependencias del proyecto en un fichero de requisitos para que otros puedan reproducir tu entorno. Investiga cómo se genera con `pip`.
- Otras herramientas del cap. 2: **Jupyter Notebook** (cuadernos interactivos, muy usados en ciencia de datos), **WSL** (Linux dentro de Windows) y **VSCode** (atajos de teclado y depurador, pp. 37-46).