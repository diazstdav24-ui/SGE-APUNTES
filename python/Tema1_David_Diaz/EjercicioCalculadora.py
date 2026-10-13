

num1 = float(input("Diga el primer número: \n"))
num2 = float(input("Diga el segundo número: \n"))

repeat = True


while repeat:

    choose = int(input("Qué desea hacer con los números \n1.Sumar \n2.Restar \n3.Multiplicar \n4.Dividir \n0.Salir \n"))
    
    match choose: 
        
        case 1 : 
            
            print(f"\n {num1 + num2} \n")
        
        case 2 :
        
            print(f" \n {num1 -  num2} \n")
        
        case 3: 
            
            print(f" \n {num1 * num2} \n")
        
        case 4 : 
            
            print(f"\n {num1 / num2} \n")
            
        case 0 :
            
            repeat = False
            
            print("Hasta luego!")
            
                
            
            
            

