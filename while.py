# while y for

# Anteriormente vimos que un for se ejecuta determinado
# numero de ocasiones segun sean los elementos de una
# coleccién (como un arreglo)

# En la mayoria de lenguajes existe el while que se ejecuta
# mientras una condici6én sea verdadera

pregunta = 'agrega un numero y te diré si es par o non \r\n'
pregunta += '(escribe "cerrar" para salir de la palicacion) \r\n'
preguntar = True

while preguntar:

    numero  = input ('agrega un numero y te diré si es par o non \r\n')

if numero == 'cerrar':
    preguntar = False
else:
    numero = int (numero)

    numero  = int (numero)


if numero % 2 == 0:
    print(f'el numero {numero} es par')
else:
    print(f'el numero {numero} es impar')



numero = 0

while numero <=10:
    print(numero)
    numero +=1 #incremento para evitar un loop infinito

    #if dentro de while

while numero <=10:
    if numero == 5:
        print('cinco')
        break
    else:
        print(numero)
    numero +=1
   
