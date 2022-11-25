# una funcion que esta dentro de una clase pasa a ser un metodo

class Restaurant:
    def __init__(self,nombre, categoria,precio): #esto es el constructor
        self.nombre = nombre 
        self.categoria = categoria
        self.precio = precio

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria:{self.categoria}, Precio: {self.precio}')

#Instanciando la clase. ES CUANDO MANDO A LLAMAR LA FUNCION.
restaurant = Restaurant('Pizzeria Mexico','comida italiana', 1.45)
restaurant.mostrar_informacion()

restaurant2 = Restaurant('Hamburguesa Python', 'comida casual', 2.30)
restaurant2.mostrar_informacion()


#   ABSTRACCION
# Son los datos necesarios de una
# Clase, si elaboras un menú de un
# restaurant es necesario el nombre
# de platillo, descripcién y precio,
# otros datos como el color favorito
# del Chef no son necesarios.