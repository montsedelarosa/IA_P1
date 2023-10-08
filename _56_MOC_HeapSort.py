# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

#Este es un ejemplo de un programa de ordenamiento Heapsort en Python:

def heapsort(arr):
    def heapify(arr, n, i):
        # Inicializamos el índice más grande como la raíz
        mayor = i
        izquierda = 2 * i + 1
        derecha = 2 * i + 2

        # Comparamos con el hijo izquierdo
        if izquierda < n and arr[i] < arr[izquierda]:
            mayor = izquierda

        # Comparamos con el hijo derecho
        if derecha < n and arr[mayor] < arr[derecha]:
            mayor = derecha

        # Si el mayor no es la raíz, lo intercambiamos
        if mayor != i:
            arr[i], arr[mayor] = arr[mayor], arr[i]

            # Heapify recursivamente el subárbol afectado
            heapify(arr, n, mayor)

    n = len(arr)

    # Construimos un max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extraemos elementos uno por uno
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Intercambiamos el elemento máximo (raíz) con el último elemento
        heapify(arr, i, 0)  # Llamamos a heapify en el subárbol reducido

# Ejemplo de uso:
arr = [12, 11, 13, 5, 6, 7]
heapsort(arr)
print("Arreglo ordenado por Heapsort:")
print(arr)
