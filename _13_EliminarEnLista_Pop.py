#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ coding: utf-8 _*_

colores = ['rojo', 'azul', 'verde', 'amarillo'] #Elementos de la lista a mostrar
colores.pop() #Con la función 'pop()' podemos eliminar el ultimo valor de la lista a la hora de imprimir
print(colores) #imprime la lista

#A su vez, con el método 'Pop()' se puede eliminar un elemento de la lista específico y almacenar el elemento eliminado en una variable, este se mostrara al imprimirlo

colores1 = ['rojo', 'azul', 'verde', 'amarillo'] #Elementos de la lista a mostrar
almacena_valor = colores1.pop(2) #Con la función 'pop()' y señalando el numero 2 le decimos a python que el valor 2 de la lista deberá ser almacenado en la variable asignada
print('El color eliminado y almacenado es:', almacena_valor) #imprime el valor almacenado en la variable 2