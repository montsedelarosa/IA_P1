# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

# Este es un ejemplo de un programa de ordenamiento por inserción en Python:

def ordenamiento_insercion(arr):
    # Recorremos la lista desde el segundo elemento hasta el final
    for i in range(1, len(arr)):
        # Almacenamos el valor actual en una variable temporal
        valor_actual = arr[i]
        # Inicializamos un índice para comparar con los elementos anteriores
        j = i - 1
        # Comparamos el valor actual con los elementos anteriores y desplazamos los elementos mayores hacia la derecha
        while j >= 0 and valor_actual < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # Colocamos el valor actual en su posición correcta
        arr[j + 1] = valor_actual

# Ejemplo de uso:
arr = [12, 11, 13, 5, 6]
ordenamiento_insercion(arr)
print("Arreglo ordenado por inserción:")
print(arr)
