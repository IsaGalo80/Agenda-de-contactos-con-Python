#        HERENCIA
# Puedes crear una clase que sea
# hijo o una copia de otra, al
# heredar una clase tendras todos
# los métodos y atributos de la
# clase padre en el hijo, y podras
# modificarlos en caso de ser
# necesario.
class Restaurant:
    def __init__(self,nombre, categoria,precio): 
        self.nombre = nombre 
        self.categoria = categoria
        self.__precio = precio 

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria:{self.categoria}, Precio: {self.__precio}')
    
    def get_precio(self):#para acceder aprecio o categoria
        print(self.__precio)
    
    def set_precio(self,precio):
        self.__precio = precio


#Instanciando la clase. ES CUANDO MANDO A LLAMAR LA FUNCION.
restaurant = Restaurant('Pizzeria Mexico','comida italiana', 50)
restaurant.__precio = 80 
restaurant.mostrar_informacion()
restaurant.set_precio(80)
restaurant.get_precio()

restaurant2 = Restaurant('Hamburguesa Python', 'comida casual', 20)
restaurant2.__precio = 40
restaurant2.mostrar_informacion()
restaurant2.set_precio(40)
restaurant2.get_precio()

#crear una clase hijo de restaurant

class Hotel (Restaurant):
    def __init__(self,nombre, categoria,precio): 
        super().__init__(nombre, categoria, precio)


    hotel = Hotel('Hotel Poo', '5 Estrellas', 200)
    hotel.mostrar_informacion()
        