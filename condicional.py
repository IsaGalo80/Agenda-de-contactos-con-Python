 #operadores que se pueden utilizar para evaluar una condición
 #==
#  !=diferente
#  > mayor a 
#  >= mayor o igual a 
#  < menor 
#  <= menor o igual a 

# Ejemplo de if en python 

# balance = 500

# if balance >0:
#     print('puedes pagar')

# revisar si una condicion es mayor a 
balance = 0

if balance >0:
    print('puedes pagar')

#if ...else

if balance >0:
    print('puedes pagar')
else:
    print('no tienes saldo')

    #likes
    likes =200

    if likes >=200:
        print('excelente, 200 likes')
    else:
        print ('casi llegas a los 200')

#if con texto

lenguaje = 'PHP'
if not lenguaje == 'python':
    print('excelente decision')


#evaluar boolean
usuario_autenticado = True
if usuario_autenticado:
    print('Acceso al sistema')
else: 
    print('debes iniciar sesión')


