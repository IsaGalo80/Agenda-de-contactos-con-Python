# POLIMORFISMO
# Es la habilidad de tener diferentes comportamientos 
# basado en que subclase se esta utilizando, relacionado 
# muy estrechamente con herencia

class Restaurant:
    def __init__(self,nombre, categoria,precio): 
        self.nombre = nombre #atributos linea 8, 9, 10
        self.categoria = categoria
        self.precio = precio 

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria:{self.categoria}, Precio: {self.precio}')
    
    def get_precio(self):#para acceder aprecio o categoria
        print(self.precio)
    
    def set_precio(self,precio):
        self.precio = precio


#Instanciando la clase. ES CUANDO MANDO A LLAMAR LA FUNCION.
restaurant = Restaurant('Pizzeria Mexico','comida italiana', 50)
restaurant.precio = 80 
restaurant.mostrar_informacion()
restaurant.set_precio(80)
restaurant.get_precio()

restaurant2 = Restaurant('Hamburguesa Python', 'comida casual', 20)
restaurant2.precio = 40
restaurant2.mostrar_informacion()
restaurant2.set_precio(40)
restaurant2.get_precio()

#crear una clase hijo de restaurant

class Hotel (Restaurant):
    def __init__(self,nombre, categoria,precio,alberca): 
        super().__init__(nombre, categoria, precio)
        self.alberca = alberca

        #REESCRIBIR UN METODO DEBE LLAMARSE IGUAL

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria:{self.categoria}, Precio: {self.precio}, Alberca: {self.alberca}')
    


#AGREGAR UN METODO QUE SEA ESPECIFICO DE HOTEL
    def get_alberca(self):
        return self.alberca

    hotel = Hotel('Hotel Poo','5 Estrellas', 200, 'Si')
    hotel.mostrar_informacion()
    alberca = hotel.get_alberca()
    print(alberca)
        