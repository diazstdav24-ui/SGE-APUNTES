
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

