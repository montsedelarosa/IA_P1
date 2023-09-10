#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ coding: utf-8 _*_

# Elif: En caso de requerir añadir más condiciones se implementa la función 'elif()'
# Input: Con la función 'input()' el usuario será capaz de interactuar con el programa

edad = int(input('¿Que edad tienes?\n')) #Valor de la variable asignada por el usuario, esto es posible gracias a la función input()
if edad <=0: #Primera condición 
    print('Nadie puede tener esa edad.') #Si la primer condición es falsa (menor o igual a 0) mostrara este mensaje 
elif edad >=1 and edad <=17: #Primer condición adicional con la función elif
    print('Eres menor de edad.') #Si se cumple mostrara este mensaje
elif edad >=18 and edad <=100: #Segunda condición adicional con la función elif
    print('Eres mayor de edad.') #Si la se cumple mostrara este mensaje
else: 
    print('Edad no valida.') #En caso de no ser ninguna de las anteriores mostrara este mensaje 