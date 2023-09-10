# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

# KWARGS: Cuando queremos utilizar argumentos arbitrarios en diccionarios, *args no nos va a servir, ya que los diccionarios constan de dos partes, las claves y los valores. En este caso, necesitas usar **kwargs.

def colores (**kwargs): #argumento de palabra clave: nos evita tener que escribir los argumentos de nuevo, asi puedes usar cuantos argumentos quieras
	print("Este es el color " + kwargs['color1'] + '.') #se mandan llamar los argumentos seleccionados y los imprime

colores(color1='rojo', color2='azul') #reclara los argumentos 