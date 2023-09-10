#Formas de abreviar condicionales en python 

#Código sin abreviaciones

x = 100 #Valor de la variable 
y = 200 #Valor de la variable 
x1 = 300 #Valor de la variable
y1 = 300 #Valor de la variable

if x < y:
    print('x es menor que y.') #Condición  inicial 

#Con abreviaciones

if x < y: print('x es menor que y.') #Condición inicial abreviada

#Con abreviaciones + else

print('x es menor que y.') if x < y else print('x no es menor que y') #Condición inicial abreviada (verdadera)
print('x es menor que y.') if x1 < y1 else print('x no es menor que y.') #Condición inicial abreviada (falsa)