# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

#MÉTODO _INIT_: Método especial que podemos poner en las clases para establecer unos valores iniciales a los objetos que se creen a partir de la clase que lo contenga.

class Usuarios: #crea una clase
	def __init__(self, nombre, pin): #argumenots obligatorios. __Init__ especifica argumentos por defecto
		self.nombre=nombre
		self.pin=pin

	def saludo(self): #clase 1 creada, self es para hacer referencia al argumento que se crea después
		print("Saludos " + self.nombre + ". Iniciaste sesión correctamente.") #mensaje a imprimir
    
	def despedida(self): 
		         print("Nos vemos " + self.nombre + ", cerraste la sesión.") #mensaje a imprimir

usuario1=Usuarios('Montse', 'ceti12345678') #objeto pertenesiente a la clase usuario


usuario2=Usuarios('Daniel', '2205199224') #objeto pertenesiente a la clase usuario

usuario1.saludo() #imprime saludo a usuario 1
usuario2.saludo() #imprime saludo a usuario 2
usuario1.despedida() #imprime despedida a usuario 1
usuario2.despedida() #imprime despedida a usuario 2


