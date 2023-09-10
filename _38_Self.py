# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

#SELF: cambiar valores ya establecidos en objetos

class Usuario: #Crear una clase 
	def __init__(self, nombre, apellidos): #Método 1: aqui se usa el primer self 
		self.nombre = nombre
		self.apellidos = apellidos

	def imprime_datos(self): #Método 2: el sel futilizado en este metodo no es el mismo que el del método 1
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

usuario001 = Usuario('Montserrat', 'De La Rosa Alvarez') #Crea un objeto 

usuario002 = Usuario('Arturo ', 'Rojas Cervantes')

usuario002.nombre = 'Yosue' #cambia el nombre del usuario002

usuario002.imprime_datos() #imprime los datos del usuario

