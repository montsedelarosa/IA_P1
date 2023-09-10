# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

class Usuario: #define la clase y su nombre con class
	nombre = '' #atributo 1
	apellidos = '' #atributo 2

	def imprime_datos(self): #imprime los valores de los atributos de la clase.
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

a21110448 = Usuario() #se crea un objeto a partir de la clase dándole un nombre (usuario001).

a21110448.nombre = 'Montserrat' #asigna nombre
a21110448.apellidos = 'De La Rosa Alvarez' #asigna apellido

a21110448.imprime_datos() #imprime los objetos 