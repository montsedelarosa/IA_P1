# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

# Este es un ejemplo de un programa de ordenamiento por burbuja en Python:

def ordenamiento_burbuja(arr):
    n = len(arr)
    # Recorremos el arreglo n veces
    for i in range(n):
        # Últimos i elementos ya están en su lugar, por lo que no necesitamos compararlos
        for j in range(0, n-i-1):
            # Comparamos elementos adyacentes y los intercambiamos si están en el orden incorrecto
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Ejemplo de uso:
arr = [64, 34, 25, 12, 22, 11, 90]
ordenamiento_burbuja(arr)
print("Arreglo ordenado por burbuja:")
print(arr)
