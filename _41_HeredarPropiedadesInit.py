# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

class Usuarios: 
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def muestra_datos(self):
        print("El nombre de usuarios es: " + self.nombre, "y tiene", self.edad, "años.")

usuario1 = Usuarios("Enrique", 28)

usuario1.muestra_datos()

class Usuarios_premium(Usuarios):
    def __int__(self, nombre, edad, instagram):
        Usuarios.__int__(self, nombre, edad)
        self.instagram = instagram
    
    def muestra_datos_premium(self):
        print("El nombre de usuario es: " + self.nombre, "y tiene", self.edad, "años. Su instagram es:", self.instagram)

usuario2 = Usuarios_premium("Elvira", 23, "elvi_23")

usuario2.muestra_datos_premium()