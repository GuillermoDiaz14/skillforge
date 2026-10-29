print("***Funciones en python***")
def saludar(nombre:str):
    print("Hola",nombre)

#Programa principal
nombre = input("Cual es tu nombre? ")
print('llamando a la funcion desde el programa principal')
saludar(nombre)