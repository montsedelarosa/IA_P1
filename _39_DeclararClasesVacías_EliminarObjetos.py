# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

# En este capítulo aprenderás a dejar clases vacías con pass, a eliminar propiedades a los objetos y como eliminar objetos completamente en Python.

# Dejar una clase vacía

class nombreclase (): #palabra reservada en la clase
    pass #deja la clase vacia 

# Eliminar una propiedad de un objeto 


class Usuarios: #clase definida 
    def __init__(self, nombre, edad):  #atributos de la clase
        self.nombre = nombre #atributo 1
        self.edad = edad #atributo 2

    def muestra_datos(self): #muestra los datos de la clase 
        print("El nombre de usario es: " + self.nombre, self.edad) #imprime este mensaje 

usuario1 = Usuarios("Jaime.", 28) #declaramos en nombre del objeto 

print(usuario1.nombre, usuario1.edad) #imprime nombre y edad 

del usuario1.edad #elimina la propiedad 'edad'

print(usuario1.nombre, usuario1.edad) #manda a llamar los atributos para imprimiros, pero al aplicar 'del' para eliminar la edad este marcara un error 

#Eliminar un objeto 

class Usuarioss: #clase definida 
    def __init__(self, nombre1, edad1):  #atributos de la clase
        self.nombre1 = nombre1 #atributo 1
        self.edad1 = edad1 #atributo 2

    def muestra_datos(self): #muestra los datos de la clase 
        print("El nombre de usario es: " + self.nombre1, self.edad1) #imprime este mensaje 

usuario2 = Usuarioss("Jaime.", 28) #declaramos en nombre del objeto 

print(usuario2.nombre1, usuario2.edad1) #imprime nombre y edad 

del usuario2.edad1 #elimina la propiedad 'edad'

print(usuario2.nombre1, usuario2.edad1) #manda a llamar los atributos para imprimiros, pero al aplicar 'del' para eliminar la edad este marcara un error 
