
import numpy

numeros = []

continuar = True

cont = 1

cont_negativos = 0

while continuar : 
    
    
    
    opcion = int(input('¿Desea añadir un nuevo número?\n 1.Y 2.N '))
    
    match opcion: 
        
        case 1: 
            
            numeros.append(input(f'Diga el número {cont} \n'))

            
            cont += 1
        
        case 2:
            
            continuar = False
        
        case _: 
            
            print('El número seleccionado debe de ser 1 o 2') 

print('Lista de números:') 
for numero in numeros:
    
    print(numero)
    
print('Lista de números sin negativos: ')
for numero in numeros:
    
    if int(numero) < 0: 
        
      numeros[numeros.index(numero)] = 0
        
        
    
        
                
        
    
    
    