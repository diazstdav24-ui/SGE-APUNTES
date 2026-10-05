# Jugador 1
print("Opciones: ")
print("1 .Tijeras")
print("2. Piedra")
print("3. Papel")

choose = int(input('Usuario uno, selecciona una opción: \n'))

match choose:
    case 1:
        choose = "tijeras"
    case 2:
        choose = "piedra"
    case 3:
        choose = 'papel'
    case _:
        print('Tienes que seleccionar una de las opciones \n')
        choose = None

# Jugador 2
print("Opciones: ")
print("1 .Tijeras")
print("2. Piedra")
print("3. Papel")

choose2 = int(input('Usuario dos, selecciona una opcion'))

match choose2:
    case 1:
        choose2 = "tijeras"
    case 2:
        choose2 = "piedra"
    case 3:
        choose2 = 'papel'
    case _:
        print('Tienes que seleccionar una de las opciones')
        choose2 = None


match choose: 
    case "tijeras": 
        match choose2:
            case "tijeras":
                print('Empate')
            case "piedra": 
                print('Gana el jugador dos')
            case "papel": 
                print('Gana el jugador uno')
    case "papel":
        match choose2: 
            case "tijeras":
                print('gana el jugador dos')
            case "piedra":
                print('gana el jugador dos')
            case "papel":
                print('Empate')
    case "piedra":
            match choose2:
                case "tijeras":
                    print('gana el jugador uno')
                case "piedra":
                    print('emapte')
                case "papel":
                    print('gana el jugador dos')