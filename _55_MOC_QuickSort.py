# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

# Este es un ejemplo de un programa de ordenamiento Quicksort en Python:

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    # Elegimos un elemento pivote (en este caso, el último elemento del arreglo)
    pivot = arr[-1]
    
    # Creamos listas para los elementos menores, iguales y mayores que el pivote
    menores, iguales, mayores = [], [], []
    
    for elemento in arr:
        if elemento < pivot:
            menores.append(elemento)
        elif elemento == pivot:
            iguales.append(elemento)
        else:
            mayores.append(elemento)
    
    # Llamamos recursivamente a quicksort en las listas menores y mayores
    return quicksort(menores) + iguales + quicksort(mayores)

# Ejemplo de uso:
arr = [12, 4, 5, 6, 7, 3, 1, 15]
resultado = quicksort(arr)
print("Arreglo ordenado por Quicksort:")
print(resultado)
