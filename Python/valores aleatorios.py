#formas para implementar la funcion
#import random #es la manera corta
from random import randint #manera larga

#dado de 6 caras
numero=randint(1,6)

#resultado
print(f"Numero aleatorio: {numero}")


#Ejemplo: Generador de ID unico para un usuario
nombre=input("Ingresa tu nombre: ")
apellido=input("Ingresa tu apellido: ")
anio_nacimiento=int(input("Ingresa tu año de nacimiento: "))

#numero aleatorio entre 1 y 100
numero_aleatorio=randint(1000,9999)

#Slicing
id=nombre.upper()[0:2]+apellido.upper()[0:2]+str(anio_nacimiento)[-2:]+str(numero_aleatorio)

#Resultado::
print(f"Tu id es: {id}")