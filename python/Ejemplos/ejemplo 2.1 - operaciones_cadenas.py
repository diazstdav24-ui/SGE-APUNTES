
proverb1 = 'Cuando el río suena'
proverb2 = 'agua lleva'

print(proverb1 + proverb2)

proverb = proverb1 + proverb2

#Una cadena es como si fuese un array de letras 

print(proverb1 +  ', ' + proverb2)

#Repetir
reaction = 'wow '

print(reaction * 4)

#Uso de índices

sentence = 'Hola, mundo'
print(sentence[0])
print(sentence[-1])
print(sentence[4])
print(sentence[-5])


'''
Las cadenas de texto son tipos de datos inmutables. 
Es por ello que no podemos modificar un carácter directamente

'''

#Trocear una cadena 

print(proverb [:])
print(proverb[12:])
print(proverb[5:12])
print(proverb[5:11:12])

#Obtener la longitud de una cadena 

print(len(proverb))

empty = ''
len(empty)

#Pertenencia a un elemento

print('suena' in proverb)

#Para cuando no pertenece
print(not('conocer' in proverb))

#Dividir una cadena

print(proverb.split())

#Split devuelve una lista
print(type(proverb.split(',')))

#Limpiar cadenas

serial_number =  '\n\t \n 121231331323 \n\n\n\t'

print(serial_number)

print(serial_number.strip)

#Existén varíables com por ejemplo: left strip o right strip 

#Comprobar si una cadena de texto empieza o termina por alguna subcadena
lyrics = 'Y por eso esperaba con la carita empapada que llegaras con rosas'

print(lyrics.startswith('y'))

print(lyrics.endswith('adios'))

#Encontrar la primera ocurrencia de alguna subcadena

print(lyrics.find('por'))
print(lyrics.index('por'))

#contabilizar el mnúmero de veces que aparece una subcadena

print(lyrics.count('con'))

#Reemplazar elementos
print(proverb.replace('suena', 'lleva'))

proverb.replace('mal','bien',1) #sólo1reemplazo

# ---------- Identificando caracteres ----------
# Todos devuelven True/False y comprueban TODOS los caracteres de la cadena

print('R2D2'.isalnum())    
print('C3-PO'.isalnum())     

print('314'.isnumeric())     
print('3.14'.isnumeric())    
print('abc'.isalpha())       
print('a-b-c'.isalpha())   

print('BIG'.isupper())         
print('small'.islower())       
print('First Heading'.istitle()) 
# ---------- Interpolación con f-strings ----------
name = 'Elon Musk'
age = 49
fortune = 43_300
print(f'Me llamo {name}, tengo {age} años y una fortuna de {fortune} millones')

# Para escribir llaves literales hay que duplicarlas
x = 10
print(f'The variable is {{ x = {x} }}')

# Formato de enteros
mount_height = 3718
print(f'{mount_height:10d}')    
print(f'{mount_height:010d}')    
# Otras bases
value = 0b10010011
print(f'{value}')               
print(f'{value:b}')              

# Formato de flotantes
pi = 3.14159265
print(f'{pi:f}')                
print(f'{pi:.3f}')               
print(f'{pi:7.2f}')               
print(f'{pi:07.2f}')           
print(f'{pi:e}')                
# Alineación
text1, text2, text3 = 'how', 'are', 'you'
print(f'{text1:<7s}|{text2:^11s}|{text3:>7s}')     
print(f'{text1:-<7s}|{text2:·^11s}|{text3:->7s}')  

# Modo debug (Python 3.8+): muestra nombre = valor
serie = 'The Simpsons'
imdb_rating = 8.7
print(f'{serie=}')
print(f'{imdb_rating=}')

# Modo representación: !r muestra el objeto tal como se almacena (con comillas)
name = 'Steven Spielberg'
print(f'{name!r}')

