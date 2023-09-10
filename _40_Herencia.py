# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

# HERENCIA: La herencia nos permite que una clase obtenga propiedades de otra clase. En general, la herencia se utiliza para ahorrarnos código y evitar tener que repetir cosas.
#En la herencia, llamamos a la clase de la cual heredan otras clases, clase padre, clase base, principal o superclase. Puedes llamarla como quieras.
#A las que reciben la herencia se les llama clases hijo, derivadas, secundarias o subclases.


#CLASE PADRE

class Usuarios: #clase definida 
    def __init__(self, nombre, edad):  #atributos de la clase
        self.nombre = nombre #atributo 1
        self.edad = edad #atributo 2

    def muestra_datos(self): #muestra los datos de la clase 
        print("El nombre de usario es: " + self.nombre, "y tiene", self.edad) #imprime este mensaje 

usuario1 = Usuarios("Jaime", 28) #declaramos en nombre del objeto 

usuario1.muestra_datos()

#CLASE HIJO

class Usuarios_premium(Usuarios): #tiene las mismas funcionalidades que la clase 'Usuarios' pero abrevida y perteneciente a la clase 'Usuarios_premium'
    pass 

usuario2 = Usuarios_premium("Ana", 63) #cambia el valor de la clase padre por el valor de la subclase, o sea 'Ana, 63'

usuario2.muestra_datos() #imprime lo definido en la subclase
