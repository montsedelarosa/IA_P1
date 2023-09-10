#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ coding: utf-8 _*_

# MÉTODO SORT() - Ordena alfabéticamente los elementos de la lista (los cambios de Sort son permanentes)

colores = ['rojo', 'azul', 'verde', 'amarillo'] #Elementos de la lista a mostrar
colores.sort() #Modo de implementar la función Sort() 
print(colores) #Imprime los elementos de lista

#Si se quiere ordenar en orden descendente (z-a) añadir 'reverse=True' dentro del método 'Sort()'

colores = ['rojo', 'azul', 'verde', 'amarillo'] #Elementos de la lista a mostrar
colores.sort(reverse=True) #Modo de implementar el 'reverse=True', debe ser dentro dle parentesis de la funcion Sort() y con la T mayúscula
print(colores) #Imprime los elementos de lista

# MÉTODO SORTED() - Ordena alfabéticamente los elementos de la lista (los cambios de Sorted son temporales)

colores = ['rojo', 'azul', 'verde', 'amarillo'] #Elementos de la lista a mostrar
print(sorted(colores)) #Función Sorted() aplicada, esta solo afecta a la propia línea (ordena los valores alfabéticamente)
print(colores) #Imprime la lista en el orden predeterminado escrito en la variable