"""
Vas a programar el sistema de venta de entradas de un cine pequeño. El programa trabaja con un menú y con una cadena de texto que contiene la cartelera.

Datos de partida (decláralos tú al principio del programa):

Una cadena con la cartelera, con las películas separadas por comas, por ejemplo "Dune,Oppenheimer,Barbie,Alien,Up"
El precio base de la entrada, que es un número decimal (7.5)
Un booleano que indique si hoy es el día del espectador
Apartado 1: Menú principal (control de flujo)

Muestra un menú que se repita hasta que el usuario elija salir:

Ver cartelera
Comprar entradas
Buscar película
Código secreto
Salir

Tienes que usar match-case para gestionar la opción elegida. Si la opción no existe, debe mostrarse un mensaje de error. La opción del usuario llega como texto desde input(), así que piensa en qué tipo necesitas para comparar.

Apartado 2: Ver cartelera
Trocea la cadena de la cartelera para tener cada película por separado.
Muéstralas numeradas, empezando en 1, con este formato: Película 1: DUNE (4 letras).
Debajo de la lista, dibuja una línea separadora de 30 guiones sin escribir los 30 guiones a mano.

Apartado 3: Comprar entradas
Pide cuántas entradas quiere el usuario y conviértelo a número.
Pide la edad del comprador.
Calcula el precio con estas reglas:
Menores de 12 o mayores de 65 pagan la mitad.
Si es el día del espectador y no es menor de 12, se aplica un 20 % adicional de descuento.
Si compra más de 5 entradas, se le avisa de que es una compra de grupo.
Usa el operador morsa en alguna de las condiciones (por ejemplo, calculando y comprobando un valor a la vez).
Muestra el total con una f-string, con exactamente 2 decimales: Total a pagar: 22.50 €.
Muestra también qué tipo tiene el resultado si multiplicas el número de entradas (entero) por el precio (decimal).

Apartado 4: Buscar película
Pide al usuario un texto y comprueba si aparece en la cartelera (sin distinguir mayúsculas y minúsculas).
Si aparece, recorre la cartelera película a película y, cuando la encuentres, deja de buscar y muestra en qué posición estaba.
Si el bucle termina sin encontrarla, muestra “No está en cartelera”. Hazlo de dos formas: una con el else del bucle y otra con una variable bandera (flag).

Apartado 5: Código secreto
El usuario introduce una palabra. El programa debe:

Recorrerla letra a letra y contar cuántas vocales tiene, saltándose los espacios (usa continue).
Mostrar la palabra al revés usando troceado (slicing).
Mostrar solo las letras que están en posiciones pares.
Mostrar la primera y la última letra.
Usando range con los tres parámetros, mostrar una cuenta atrás desde la longitud de la palabra hasta 1.

"""



peliculas = "Dune, Openheimmer, Barbie, La bola negra, Up"

continuar = True
cont = 0

precio_base = 7.5
dia_espectador = False

total = 0.0 

pelis_troceadas = ""

print('Bienvenido a tu cine de confianza')

while continuar: 
    
   opcion = int(input("¿Que desea hacer? \n1.Ver cartelera \n2.Comprar entradas \n3.Buscar películas \n4.Codigo secreto \n0.Salir \n"))
   
   match opcion:
       
    case 1: 
           
        pelis_troceadas = peliculas.split(",")
            
        print(f'La cartelera: \n   ')
            
        for peli in pelis_troceadas:
                
            print(f'Pelicula {cont}: {peli} {len(peli)} \n')
                
            cont = cont + 1
            
        print("-"*30)
    case 2: 
        
        num_entradas = int(input("¿Cuantas entradas deseas? \n"))
        
        edad_comprador = int(input("La edad el comprador \n"))
        
        respuesta = int(input('¿Día del espectador? \n 1.Y | 2.N \n'))
        
        if respuesta == 1:
            dia_espectador = True
                
        
        if edad_comprador <= 12 or edad_comprador >= 65: 
            
            print('Aplica descuento por edad')
            precio_base /= 2


        
        elif dia_espectador and edad_comprador <= 12 or edad_comprador >= 65:
            
            print('Aplica descuento 20%')
            nuevoPrecio = precio_base * 0.2  
            
        if num_entradas > 5: 
            
            print('Es una compra en grupo')
        
        print(f'Total precio: {precio_base * num_entradas:.2f} ')  
        
        print(type(precio_base * num_entradas))
        
    case 3: 
        
        busqueda = input('Introduza el texto')      
        
        if busqueda in pelis_troceadas:
            
           print(pelis_troceadas.index(busqueda)) 
        
        else:
            
            print('No lo encuentro')
                  

            
            
        
        