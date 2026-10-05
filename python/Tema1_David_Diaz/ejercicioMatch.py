def elegir_tirada(choose):
    match choose: 
        case 1: 

            return "tijeras"


        case 2: 
            
           return "piedra"


        case 3: 

            return 'papel'


        case _:

            print('Tienes que seleccionar una de las opciones')

def opciones():
    print("Opciones: ")
    print("1 .Tijeras")
    print("2. Piedra")
    print("3. Papel")

def ejecutar_juego(tupla_choose):

    match tupla_choose



opciones()      

choose = int(input('Usuario uno, selecciona una opción'))

choose = elegir_tirada(choose)

opciones()      

choose2 = int(input('Usuario dos, selecciona una opcion'))  

choose2 = elegir_tirada(choose2)

tupla_choose = (choose, choose2)





    