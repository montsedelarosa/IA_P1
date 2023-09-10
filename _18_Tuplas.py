#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ coding: utf-8 _*_

# TUPLAS: Las tuplas son similares a las listas pero con 2 diferencias, se escriben con '()' y son inmutables (Las listas se escriben con '[]' y no son inmutables). Además, las tuplas no se pueden modificar una vez mostradas

tupla = ('rojo', 'azul', 'verde', 'amarillo') #Elementos de la tupla a mostrar
print(tupla) #Imprime los valores de la tupla

# Para acceder a las posiciones de las tuplas de python se hace lo siguiente

tupla = ('rojo', 'azul', 'verde', 'amarillo') #Elementos de la lista a mostrar
print(tupla[0]) #Mandamos llamar la posición 0 y la mostramos

# Tipos de datos soportados en las tuplas

tupla = (10, 15, 20, 'El resultado de la operación es: ') #Asignamos los valores de la variable y el mensaje que mostrara el resultado de la operación a realizar
print(tupla[3], tupla[2] + tupla[0] * tupla[1] / tupla[0]) #Llamamos al string de la posición 3 y lo concatenamos con las operaciones siguientes. Python realizara la operacion por orden de la jerarquía de operaciones 


