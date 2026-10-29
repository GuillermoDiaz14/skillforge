#Desde aqui mandaremos a traer las funciones

#Importamos
from modulo import suma

print("Calculadora")

num1=int(input("introduce el primer numero:" ))
num2=int(input("introduce el segundo numero:" ))
print("El resultado de la suma de ambos valores es", suma(num1,num2))

#Segunda manera de importar una funcion (mas larga)
import modulo
print("El resultado de la resta de ambos valores es",modulo.resta(num1,num2) )
