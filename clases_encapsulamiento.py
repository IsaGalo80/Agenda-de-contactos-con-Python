class Restaurant:
    def __init__(self,nombre, categoria,precio): 
        self.nombre = nombre 
        self.categoria = categoria
        self.__precio = precio #POR DEFECTO ES PUBLICA
        #PARA HACERLO PROTEGIDO (PROTECTED) SE LE COLOCA _...SELF.__precio = PRECIO DE ESA FORMA SI UNO SIGUE ESCRIBIRENDO CODIGO NO SE PUEDE CAMBIAR EL VALOR. PRIVATE ES CON DOBLE __ PERO RESULTA QUE ESTO DA ERROR, SE PUEDE ACCEDER DE UNA SOLA FORMA

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria:{self.categoria}, Precio: {self.__precio}')
    
    def get_precio(self):#para acceder aprecio o categoria
        print(self.__precio)
    
    def set_precio(self,precio):
        self.__precio = precio


#Instanciando la clase. ES CUANDO MANDO A LLAMAR LA FUNCION.
restaurant = Restaurant('Pizzeria Mexico','comida italiana', 50)
restaurant.__precio = 80 #esto es hacer encapsulamiento ESTO NO DEBERIA PASAR. CON PRIVATE NO ES POSIBLE MODIFICARLO. SE PUEDE MODIFICAR CON GATTERS Y SETTERS QUE SON METODOS. 
# GET OBTIENE UN VALORMIENTRAS QUE SET LO MODIFICA
restaurant.mostrar_informacion()
restaurant.set_precio(80)
restaurant.get_precio()

restaurant2 = Restaurant('Hamburguesa Python', 'comida casual', 20)
restaurant2.__precio = 40
restaurant2.mostrar_informacion()
restaurant2.set_precio(40)
restaurant2.get_precio()


#     ENCAPSULAMIENTO
# Permite restringir u ocultar el
# acceso a los datos dentro de la
# misma clase del mundo exterior

# ( usualmente se modifican via

# métodos en la misma clase )