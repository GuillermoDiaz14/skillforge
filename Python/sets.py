
#manejo y demostracion de sets
mi_set={1, 2, 3, 4, 5, 2}
print("Set original:", mi_set) #Los elementos duplicados se eliminan automáticamente
#Agregar elementos a un set
mi_set.add(6)
print("Set después de agregar un elemento:", mi_set)

#Agregar elemento DUPLICADO en un set
mi_set.add(3) #No se agregará ya que el elemento 3 ya existe en el set
print("Set después de agregar un elemento ya existente:", mi_set)

#Eliminar elementos de un set
mi_set.remove(5) #Elimina el elemento 5 del set 
print("Set después de eliminar un elemento:", mi_set)

#Comprobar si un elemento está en un set
if 4 in mi_set:
    print("El elemento 4 está en el set")
