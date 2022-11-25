# Qué es Programacion Orientada a
# Objetos (POO)?
# Es una forma de escribir c6digo que se considera de las mas efectivas.

# Cuando defines una clase deberas describir el
# comportamiento y forma de ese objeto

# objeto es la forma de referirse a la informacion creada por una 
# clase (Instancia de una clase)

# Cada instancia de la clase tendra la misma “forma” pero
# diferente informacion
#       javascript
# class Cliente {
# // resto de la clase
# }

# const cliente = new Cliente();

# PHP
# <?php
# class Cliente {
# // resto de la clase
# }
# $cliente = new Cliente();







# Terminologia
# instancia 
# El objeto que es creado al llamar una clase.

# atributo de clase
# Es una propiedad que tendran todos los objetos creados con nuestras clases

# Metodo
# Es una funcién que existe dentro de una Clase

class Restaurant:

    def agregar_restaurant(self,nombre): #self es la forma en que se va a guardar la info
        self.nombre = nombre #atributo

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}')

#Instanciando la clase. ES CUANDO MANDO A LLAMAR LA FUNCION.
restaurant = Restaurant()
restaurant.agregar_restaurant('Pizzeria Mexico')
restaurant.mostrar_informacion()


restaurant2 = Restaurant()
restaurant2.agregar_restaurant('Hamburguesa Python')
restaurant2.mostrar_informacion()

# mostrar la informacion
print(f'Nombre Restaurant: {restaurant.nombre}')
print(f'Nombre Restaurant: {restaurant2.nombre}')
