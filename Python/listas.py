print("***Listas***")

lista1 = [1, 2, 3, 4, 5]
print("Lista 1:", lista1)

print("Accediendo a un elemento de la lista:", lista1[2])  # Accediendo al tercer elemento (índice 2)
print("Accediendo a un elemento de la lista:", lista1[-1])  # Accediendo al último elemento (índice -1)
print("Longitud de la lista:", len(lista1))  # Imprimiendo la longitud de la lista

#Modificando un elemento de la lista
lista1[2] = 10
print("Lista 1 después de modificar el tercer elemento:", lista1)

#Agregando un elemento al final de la lista
lista1.append(6)
print("Lista 1 después de agregar un elemento al final:", lista1)

#Agregando un elemento en una posición específica
lista1.insert(3, 15)  # Insertando el número 15 en la posición 3
print("Lista 1 después de insertar un elemento en una posición específica:", lista1)

#Eliminando un elemento de la lista
lista1.remove(4)  # Eliminando el número 4 de la lista      
print("Lista 1 después de eliminar un elemento:", lista1)

#Eliminando un elemento por índice
del lista1[1]  # Eliminando el elemento en la posición 1
print("Lista 1 después de eliminar un elemento por índice:", lista1)

#Crear sublistas
sublista = lista1[1:4]  # Creando una sublista desde el índice 1 hasta el índice 3 el 4 no se incluye
print("Sublista de lista 1:", sublista)

#Iterar listas
print("Iterar listas")

nombres = ["Juan", "María", "Pedro", "Ana"]

for nombre in nombres:
    print("Nombre:", nombre)

#concatenar listas
lista2 = [7, 8, 9]
lista3 = lista1 + lista2        
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista 3 (concatenación de lista 1 y lista 2):", lista3)
