#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ coding: utf-8 _*_

suma = 10 + 5 + 7 #asignamos el valor a la variable, en este caso representaremos la suma de 3 digitos como se muestra
resta = 10 - 5 - 7 #asignamos el valor a la variable, en este caso representaremos la resta de 3 digitos como se muestra
multiplicacion = 10 * 5 * 7 #asignamos el valor a la variable, en este caso representaremos la multiplicación de 3 digitos como se muestra
division = 10 / 5 / 7 #asignamos el valor a la variable, en este caso representaremos la división de 3 digitos como se muestra
print("Suma: " ,suma, "\nResta: " ,resta, "\nMultiplicacion: " ,multiplicacion, "\nDivision: " ,division) #Las comillas despues de cada : es otra forma de concatenacion iplementada cuando el string cuenta con un valor numérico 

operacion = 10 - 5 * 7 / 3 + 5 #combinación de operadores
print("Resultado: " ,operacion)

operacion1 = (10 - 5) * 7 / 3 + 5 #Python respeta la jerarquía de operaciónes
print ("Resultado: " ,operacion1) 