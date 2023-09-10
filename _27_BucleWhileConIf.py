# Bucle while con condición if: combinaremos en él while el condicional if para finalizar su ejecución antes de tiempo (o no) independientemente de si la condición se cumple o no.

# BREAK: El uso del break en el bucle while

x = 1 #Valor de la variable a mostrar

while x <= 10: #Bucle while
    print(x) #imprimir el valor de la variable x
    if x == 5: #if anidado, dice que si x es igual a 5 el bucle dejara de correr
        break #Rompe el bucle segun la condición 
    x += 1 #Esto hace que el conteo vaya en incremento de 1 en 1

# Saltos con el uso de 'continue' en bucles while 

x1 = 0

while x1 < 10:
    x1 += 1
    if x1 == 5 or x1 == 7: #El if junto con el 'continue' hacen que se salte la ejecución cuando x1 vale 5 y cuando vale 7
        continue
    print(x1)




