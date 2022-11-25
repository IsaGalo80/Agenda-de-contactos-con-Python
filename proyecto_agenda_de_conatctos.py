import os

CARPETA = 'contactos/'  # CARPETA DE CCONTACTOS
EXTENSION = '.txt'  # EXTENSION DE ARCHIVOS

# CONTACTOS


class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria


def app():
    # REVISA SI LA CARPETA EXISTE O NO
    crear_directorio()

    # MUESTRA EL MENÚ DE OPCIONES
    mostrar_menu()

    # PREGUNTAR AL USUARIO LA ACCION A REALIZAR

    preguntar = True
    while preguntar:
        opcion = input('seleccione una opción: \r\n')
        opcion = int(opcion)

        # EJECUTAR LAS OPCIONES

        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print('Opción no válida, intente de nuevo')

def eliminar_contacto():
    nombre = input ('Seleccione el Conatcto que desea buscar: \r\n')

    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print ('\r\nEliminado Correctamente')
    except expression as identifier:
        print('No existe ese contacto')

     #REINICIAR LA APP
    
def buscar_contacto():
    nombre = input ('Seleccione el Conatcto que desea buscar: \r\n')

    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Información del Contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El archivo no existe')
        print(IOError)

        #REINICIAR LA APP
        app()
        pass

def mostrar_contactos():
    archivos = os.listdir(CARPETA)

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
            #IMPRIME LOS CONTENIDOS
                 print(linea.rstrip())
            #IMPRIME UN SEPARADOR ENTRE CONTACTOS
            print('\r\n')

def editar_contacto():
    print('Escribe el nombre del contacto a editar')
    nombre_anterior = input('Nombre del contacto que desea editar:\r\n')

    #REVISAR SI EL ARCHIVO YA EXISTE ANTES DE EDITARLO
    existe =existe_contacto(nombre_anterior) 

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:
            #RESTO DE LOS CAMPOS
            nombre_contacto = input('Agrega el nuevo Contacto:\r\n')
            telefono_contacto = input('Agrega el nuevo Teléfono:\r\n')
            categoria_contacto = input('Agrega la nueva Categoría:\r\n')

            #INSTANCIAR
            contacto = Contacto(nombre_contacto, telefono_contacto,categoria_contacto)

            #ESCIBIR EN EL ARCHIVO
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Nombre: ' + contacto.telefono + '\r\n')
            archivo.write('Nombre: ' + contacto.categoria + '\r\n')

            #RENOMBRAR ARCHIVO
            os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)

            #MOSTRAR MENSAJE DE EXITO
            print('\r\n Contacto editado Correctamente \r\n')

    else:
        print('Ese contacto no existe')

        #REINICIAR LA APP

        app()

def agregar_contacto():
    print('Escribe los datos para agregar el nuevo contacto')
    nombre_contacto = input('Nombre del Contacto:\r\n')

    # REVISAR SI EL ARCHIVO YA EXISTE ANTES DE CREARLO
    existe = existe_contacto(nombre_contacto)

    if not existe:

        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:


            # RESTO DE  LOS CAMPOS
            telefono_contacto = input('Agrega el Teléfono:\r\n')
            categoria_contacto = input('Categoría Contacto:\r\n')

            # INSTANCIAR LA CLASE
            contacto = Contacto(
                nombre_contacto, telefono_contacto, categoria_contacto)

            # ESCRIBIR EN EL ARCHIVO
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Nombre: ' + contacto.telefono + '\r\n')
            archivo.write('Nombre: ' + contacto.categoria + '\r\n')

            # MOSTRAR UN MENSAJE DE EXITO

            print('\r\n Contacto creado Correctamente \r\n')

    else:
        print('Ese Contacto ya existe')

        #REINICIAR LA APP
        app()



def mostrar_menu():
    print('Seleccione del Menú lo que desea hacer:')
    print('1) Agregar Nuevo Contacto')
    print('2) Editar Contacto')
    print('3) Ver Contactos')
    print('4) Buscar Contacto')
    print('5) Eliminar Contacto')


def crear_directorio():
    if not os.path.exists(CARPETA):
        # CREAR CARPETA
        os.makedirs(CARPETA)


def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)
app()
