#un arreglo permite agrupar diferente informacion en un solo lugar. Usualmente un array
# puede contener cualquier tipo de dato e incluso datos que no sean muy realcionados entre si.
# en python no existen los arrays, en su lugar existen los list.

#en js     const meses = ["enero", "febrero",...];
#en PHP     $meses = ["enero", "febrero",...];
#en python   meses = ["enero", "febrero",...]; para acceder tendria que poner meses [0]// esto me daria enero

lenguajes = ['python', 'Kotlin', 'java', 'js']

print (lenguajes)
#los array o list cominezan en la posicion 0

lenguajes.sort()
print (lenguajes[0])

aprendiendo = f'estoy aprendiendo {lenguajes[3]}'
print (aprendiendo)

#modificar valor de un arreglo
lenguajes [2] = 'PHP'
print(lenguajes)

#agregar elemento a un array

lenguajes.append('Ruby')
print (lenguajes)

#eliminar de un list

del lenguajes[1]

print(lenguajes)

#eliminar de un list

lenguajes.pop ()
print(lenguajes)

#eliminar con popo una posicion en especifico

lenguajes.pop(0)
print(lenguajes)

#eliminar por nombre

lenguajes.remove ('php')
print(lenguajes)





