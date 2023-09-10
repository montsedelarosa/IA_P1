#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ coding: utf-8 _*_

navegadores = ['chrome', 'firefox', 'opera', 'safari'] #Elementos de la lista 
print('chrome' in navegadores) #Desde la función print buscamos si 'chrome' se encuentra en la lista, de ser así se mostrará un 'true'

print('edge' in navegadores) #Si se busca una palabra qu eno esta en la lista mostrara un 'false'

# Ejemplo implementando un input() para que el usuario interactue con el programa

entrada = input('Introduce el nombre de un navegador:\n') #Con la función 'input()' el usuario podrá buscar una palabra en la lista
navegadores = ['chrome', 'firefox', 'opera', 'safari'] #Elementos asignados a la lista
if entrada in navegadores: #Condición para la variable navegadores
    print('El navegador que buscas esta en la lista.') #Si la condición se cumple, es decir, si la palabra que el usuario busca está en la lista mostrará el siguiente mensaje 
else:
    print('El navegador que buscas no esta en la lista.') #Si la condición no se cumple, es decir, si la palabra que el usuario busca no está en la lista mostrará el siguiente mensaje 

