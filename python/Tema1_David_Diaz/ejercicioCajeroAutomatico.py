"""
 Haga un programa de la interfaz de un cajero automático. Tendrá las opciones, ver saldo, 
retirar  dinero,  comprar  entradas  e  ingresar  dinero.  En  cada  opción  se  pedirán  los  datos 
necesarios y se realizarán las operaciones adecuadas. El coste de las entradas se debe restar al 
saldo de dicha cuenta. La cuenta será creada por nosotros con un saldo inicial concreto
"""

continuar = True

saldo_disponible = 1000.0

precio_entrada = 0.0


print('Bienvenido al OsunaBank, tu banca publica')

while continuar: 
    
    print('¿Qué deseas hacer?')

    
    choose = int(input('1. Ver saldo \n 2.Retirar \n 3.Comprar entrada \n 4.ingresar dinero \n 0.Salir \n \n'))
    
    match choose: 
        
        case 1: 
            
            print(f'Tu saldo:{saldo_disponible}')
        
        case 2: 
            
            retirar = float(input('¿Cuanto dinero desea retirar?')) 
            
            if retirar > saldo_disponible :
                
                print('La cantidad introducida es mayor que el saldo disponible')
            
            else: 
                
                saldo_disponible -= retirar 

                print('Ha sido exitoso')
                print(f'Saldo restante {saldo_disponible}')
        
        case 3: 
            
            opcion2= int(input('¿Qué entrada deseas comprar?\n 1.Concierto Shakira|90€ \n 2.RadioHead|100€ \n 3. Agorazein|50€ '))
            
            match opcion2:  
                
                case 1: 
                    
                    precio_entrada = 90
                
                    if saldo_disponible < precio_entrada:
                        
                        print('No hay suficiente saldo en la cuenta')
                    
                    else:
                        
                        saldo_disponible -= precio_entrada 
                        
                        print('Ha sido exitoso')
                        print(f'Saldo restante {saldo_disponible}')
                     
                    
                case 2: 
                                        
                    precio_entrada = 100
                
                    if saldo_disponible < precio_entrada:
                        
                        print('No hay suficiente saldo en la cuenta')
                    
                    else:
                        
                        saldo_disponible -= precio_entrada 
                        
                        print('Ha sido exitoso')
                        print(f'Saldo restante {saldo_disponible}')
                    
                case 3: 
                                        
                    precio_entrada = 50
                
                    if saldo_disponible < precio_entrada:
                        
                        print('No hay suficiente saldo en la cuenta')
                    
                    else:
                        
                        saldo_disponible -= precio_entrada 
                        
                        print('Ha sido exitoso')
                        print(f'Saldo restante {saldo_disponible}')
        case 4:
            
            ingresar = float(input('¿Cuanto dinero deseas ingresar?'))
            
            if ingresar < 10 :
                
                print('La cantidad no puede ser menor a 10')
            
            else: 
                
                saldo_disponible += ingresar
                
                print('Ha sido exitoso')
                print(f'Nuevo Saldo {saldo_disponible}')
                
                
                
                    
                        
            
            
            
    