# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

def alumnos(*args): #Al escribir *args como argumento, me da la posibilidad de utilizarlo cuando quiera dentro de la función.
	print('El primer corredor es ' + args[0] + ' y el último corredor es ' + args[3] + '.') #En el print() se llama a los argumentos según su posición en la llamada (empieza a contar a partir de 0).

alumnos('Checo Perez', 'Charles Leclerc', 'Lewis Hamilton', 'Carlos Sainz') #Argumentos

