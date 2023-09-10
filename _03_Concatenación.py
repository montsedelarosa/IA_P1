# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

#Los 4 puntos anteriores te permiten utilizar acentos sin generar errores

palabra1 = 'Montserrat' #asignamos el valor a la variable que vamos a concatenar, en este caso es un nombre
palabra2 = 'Alvarez' #asignamos el valor a la variable que vamos a concatenar, en este caso es un apellido

nombre_completo = palabra1 + palabra2 #concatenamos con el simbolo + las 2 variables declaradas anteriormente 
print(nombre_completo) #la funcion predefinida print mostrara el valor asignado en la variable nombre_completo

nombre_completo = palabra1 + ' ' + palabra2 #para espaciar las palabras: añadimos un espacio entre nombre y apellido concatenando las variables y un espacio entre las comillas simples
print(nombre_completo) 
