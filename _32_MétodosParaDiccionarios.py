# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

# MÉTODO 1:Contar elementos en un diccionario con el método len()

teclado = { #Variable del diccionario
	'Categoría': 'Teclados', #Elementos del diccionario
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

print(len(teclado)) # El método len nos sirve para contar la longitud en lementos de un diccionario

# MÉTODO 2: Eliminar todo o parte de un diccionario con del

del teclado['Precio'] #Le decimos a la función 'del' que elimine el precio del teclado 1
print(teclado) #Imprimimos el diccionario sin el valor que eliminamos 

# MÉTODO 3: Añadir nuevas claves y valores a un diccionario

teclado['Color'] = 'Negro' #Nuevo valor asignado al diccionario 
print(teclado) #imprime el diccionario con el valor nuevo