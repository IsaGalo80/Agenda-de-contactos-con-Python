# Que son los Objetos
# Un objeto es en cierta medida similar a un array, te permite agrupar
# contenido de diferentes tipos de datos.
# Usualmente se accede a un elemento de un array por medio de
# su indice, en un objeto se accede por medio de una llave (key)
# Algunos lenguajes no soportan Objetos, en Python se utiliza
#    algo llamado Dictionary

#creando un diccionario simple

cancion = {
    'artista': 'metalica', #llave y valor
    'cancion': 'enter sandman',
    'lanzamiento': 1992,
    'likes': 3000
}
#acceder a los elementos del diccionario
print(cancion['artista'])
print(cancion['lanamiento'])

#mezclar con un string

artista  = cancion ['artista']
print(f'estoy escuchando a  {artista}')

print (cancion)

#agregar nuevos valores

cancion['cancion'] = 'heavy metal'
print(cancion)

#eliminar un valor

del cancion ['lanzamiento']
print (cancion)

#iniciar un diccionario vacio

jugador ={}
print(jugador)

# se une un jugador 

jugador ['nombre'] = 'juan'
jugador ['puntaje '] = 0

#incrementando el puntaje 
jugador ['puntaje'] = 100
print (jugador)

#incrementando el puntaje

jugador ['puntaje'] = 200
print(jugador)

#acceder a un valor 
print (jugador.get ('consola', 'no existe'))

#iterar en el diccionario

for llave, valor in jugador.items ():
    print(valor)

#eliminar jugador y puntaje

del jugador ['nombre']
del jugador ['puntaje']
print (jugador)