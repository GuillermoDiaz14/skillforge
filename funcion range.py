#Funcion Range
#Secuencia del 1 al 4
for i in range(5):
    print(i)    

#Secuencia del 10 al 20
for i in range(10,20+1):
    print(i)

#Secuencia del 0 al 20 de 2 en 2
for i in range(0,20+1,2):
    print(i)

#Repetir un mensaje 5 veces
for _ in range(5):#podemos usar _ como variable si no la vamos a usar
    print("Hola Mundo")

#Imprimir un triangulo de asteriscos
num_filas= int(input("Numero de filas: "))
for fila in range(1,num_filas+1):
        print(" "*(num_filas-fila),("*")*((fila*2)-1))

