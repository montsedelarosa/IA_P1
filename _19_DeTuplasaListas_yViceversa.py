#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ coding: utf-8 _*_

# Transformar de una lista a una tupla (si la transformación es correcta al imprimir la tupla estará entre '()')

lista = ['rojo', 'azul', 'verde', 'amarillo'] #Elementos de la lista a mostrar
tupla = tuple(lista) #Cambio de lista a tupla
print(tupla) #Imprime la lista convertida a tupla

#Para detectar el tipo de dato (lista o tupla) hacemos uso de la función 'type()'
 
lista = ['rojo', 'azul', 'verde', 'amarillo'] #Elementos de la lista a mostrar
tupla = tuple(lista) #Cambio de lista a tupla
print(type(tupla)) #Imprime el tipo de dato, en este caso una 'tupla'

# Transformar de una tupla a una lista 

tupla = ('rojo', 'azul', 'verde', 'amarillo') #Elementos de la tupla
lista = list(tupla) #Cambio de tupla a lista
print(type(lista)) #Imprime el tipo de dato, en este caso una 'lista'