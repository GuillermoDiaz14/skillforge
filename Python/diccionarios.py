#Demostraccion de diccionarios en pyThon

#Creacion de un diccionario
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

print("Diccionario original:", mi_diccionario)

#Acceso a los valores del diccionario
print("Nombre:", mi_diccionario["nombre"])
print("Nombre:", mi_diccionario.get("nombre")) #Usando el metodo get() para acceder a los valores del diccionario   
print("Edad:", mi_diccionario["edad"])
print("Ciudad:", mi_diccionario["ciudad"])

#Modificación de valores en el diccionario
mi_diccionario["edad"] = 31
print("Diccionario después de modificar la edad:", mi_diccionario)

#Agregar un nuevo par clave-valor al diccionario
mi_diccionario["profesion"] = "Ingeniero"
print("Diccionario después de agregar una nueva clave-valor:", mi_diccionario)

#Eliminar valores en un diccionario
del mi_diccionario['ciudad']
print("Diccionario despues de la eliminacion",mi_diccionario)
#mi_diccionario.pop('profesion') #Usando el metodo pop() tambien podemos eliminar

#Iterar los elementos de un diccionario
for llave, valor in mi_diccionario.items():
    print(f'llave:{llave}, valor:{valor}')

#Obtener valores
print('\nValores del diccionario')
for valor in mi_diccionario.values():
    print(f'- valor: {valor}')

#Obtener las llaves
print('\nLlaves del diccionario')
for llave in mi_diccionario.keys():
    print(f'llave: {llave}')