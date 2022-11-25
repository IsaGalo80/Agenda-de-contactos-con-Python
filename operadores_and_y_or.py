#operadores and y or

user_logueado = True
user_admin = False

if user_logueado and user_admin:
    print('administrador')
elif user_logueado:
    print('acceso al sistema')
else: 
    print('debes iniciar secion')


if user_logueado or user_admin:
    print('administrador')
elif user_logueado:
    print('acceso al sistema')
else: 
    print('debes iniciar secion')
