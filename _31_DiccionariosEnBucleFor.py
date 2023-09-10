# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

#Cambiar un valor del diccionario

teclado1 = { #Variable del primer diccionario
    'Categoria': 'Teclados', #'key': 'value' es el orden en el que vemos esta función del diccionario 1
    'Modelo': 'HyperX Alloy FPS Pro', #'key': 'value' es el orden en el que vemos esta función del diccionario 1
    'Precio': '89,99' #'key': 'value' es el orden en el que vemos esta función del diccionario 1
}

teclado2 = { #Variable del segundo diccionario
    'Categoria': 'Teclados', #'key': 'value' es el orden en el que vemos esta función del diccionario 2
    'Modelo': 'Corsair K55 RGB', #'key': 'value' es el orden en el que vemos esta función del diccionario 2
    'Precio': '59,99' #'key': 'value' es el orden en el que vemos esta función del diccionario 2
}

teclado1['Precio'] = '85' #Con este comando podemos cambiar el valor de un diccionario, en este caso cambiamos el 89,99 por 85
print(teclado1['Precio']) #Imprime el precio modificado

#Iterar un diccionario con el bucle for

for x in teclado2: #Bucle for que manda llamar al diccionario 'teclado 2'
    print(x) #Imprime las categorias del diccionario 

#Iterar un diccionario para devolver sus valores

for x in teclado2: #Bucle for que manda llamar al diccionario 'teclado 2'
    print(teclado2[x]) #Imprime los valores asignaos en las categorias del diccionario