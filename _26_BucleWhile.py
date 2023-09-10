# Bucle While: Se ejecutara una serie de declaraciones siempre que la condición se cumpla, que sea verdadera. Una vez se convierta en falsa, se dejara de ejecutar el código del bucle.

x = 1 #Valor de la variable a mostrar
x1 = 9 #valor de la variable a mostrar

#while x < 10: #Bucle while, este no se detendra ya que es un bucle infinito 
   # print(x) #Imprime el valor de la variable x infinitamente

#Otro ejemplo, este no es infinito (EN INCREMENTO)

while x < 10: #Bucle while, este se detendra hasta llegar al numero 9
    print(x) #Imprime el valor de la variable 
    x += 1 #Esta funcion hace que el conteo del bucle vaya en incremento, en este caso de 1 en 1 

#Otro ejemplo, este no es infinito (EN DECREMENTO)

while x1 > 0: #Bucle while, este se detendra hasta llegar al numero 9
    print(x1) #Imprime el valor de la variable 
    x1 -= 2 #Esta funcion hace que el conteo del bucle vaya en decremento, en este caso de 2 en 2
    