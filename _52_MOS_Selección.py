# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

# Este es un ejemplo de un programa de ordenamiento por selección en Python:

def ordenamiento_seleccion(arr):
    # Recorremos la lista desde el principio hasta el penúltimo elemento
    for i in range(len(arr) - 1):
        # Encontramos el índice del elemento mínimo en el subarreglo no ordenado
        indice_minimo = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[indice_minimo]:
                indice_minimo = j
        # Intercambiamos el elemento mínimo con el primer elemento del subarreglo no ordenado
        arr[i], arr[indice_minimo] = arr[indice_minimo], arr[i]

# Ejemplo de uso:
arr = [64, 25, 12, 22, 11]
ordenamiento_seleccion(arr)
print("Arreglo ordenado por selección:")
print(arr)
