# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

# Crear funciones en Python

def saluda(): #Definicimos la funcion 
	print("Bienvenidos al curso de Inteligencia Artificial.") #Todo el código que hubiese dentro de la función saluda() solo se ejecuta cuando es llamado de la forma de la última línea del código (línea 4)

saluda() #Imprime la funcion 

# Argumentos en las funciones

def saluda1(nombre, apellidos): #Solo me dejará llamar a la función saluda() si le especifico un nombre y unos apellidos. Estos pueden contener los valores que quieras, un string, un integer, un booleano, etc.
	print('Hola', nombre, apellidos) #Imprime las variables de la funcion nombre y apellido

saluda1('Montserrat', 'De La Rosa Alvarez') #Variable 1
saluda1('Ana', 'Alvarez Hernández') #Variable 2