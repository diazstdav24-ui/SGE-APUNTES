'''
Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga 
cuántas veces aparece esa palabra en la lista. 
'''

continuar = True


palabras = []


while continuar: 

   palabra = (input(f'Diga la palabra: \n'))

   apariciones = int(input(f'¿Cuántas veces aparece la palabra: {palabra}? \n'))

   for  i in range(0, apariciones):

    palabras.append(palabra)
     
   opcion = input('¿Desea seguir? Y/N \n ')

   
   if opcion.lower().strip() == 'n':

    continuar = False


for indice in palabras:

  print(indice)

   

       