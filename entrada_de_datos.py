# La mayoria del cédigo que escribas tiene como fin solucionar
# un problema de un usuario.

# Publicar en tu muro, realizar un examen en linea, subir una
# imagen, solicitar un taxi, crear un evento, realizar un pago,
# son acciones que requieren entrada de datos por parte del
# usuario.

# En Python se utiliza la funcion input() para que detener la
# ejecucioén dele programa hasta que el usuario agregue
# informaciion

nombre = input ('cual es tu nombre: \r\n')

print(f'hola {nombre}')

#leer datos que seran numeros
edad = input('cual es tu edad?')
edad = int (edad)

if edad >=18:
    print('ya puedes votar')
else:
    print('aun no puedes votar ')

    #mezclar con operadores

    numero  = input ('agrega un numero y te diré si es par o non \r\n')

    numero  = int (numero)


if numero % 2 == 0:
    print(f'el numero {numero} es par')
else:
    print(f'el numero {numero} es impar')

    print(2 % 2)
