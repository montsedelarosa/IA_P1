#Diccionarios: Es capaz de almacenar en él una colección de objetos con claves y valores.

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

consulta = teclado1['Modelo'] #Con esta función mandamos llamar el 'key' modelo del primer diccionario
print(consulta) #Imprimimos lo que mandamos llamar 

print(teclado1) #Con esto imprimimos el diccionario completo