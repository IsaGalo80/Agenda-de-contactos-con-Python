#evaluar un elemento de la lista 

lenguajes = ['python', 'kotlin', 'java', 'js']

if 'php' in lenguajes:
    print ('php si existe')
else:
    print('no esta en la lista')

#if anidados

usuario_autenticado = True
usuario_admin = True

if usuario_autenticado:
    if usuario_admin:                #un if dentro de otro
         print('Acceso total')

    else:
        print('Acceso al sistema')
else: 
    print('debes iniciar sesión')


# If elif else en Python
# ocupacion = 'Estudiante'
# if ocupacion == 'Estudiante':
# print('Tienes 50% de descuento')
# elif ocupacion == 'Jubilado':
# print('Tienes 75% de Descuento')
# else:
# print('Debes pagar el 100%)

#ejemplo con elif

ocupacion = 'estudiante'

if ocupacion == 'estudiante':
    print('tienes 50% de dscuento')
elif ocupacion =='jubilado':
    print('tienes 75 % de descuento')
elif ocupacion == 'desempleado':
    print('tienes un 10 % d descuento')
else:
    print('dbes pagar el 100%')
