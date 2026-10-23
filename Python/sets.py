
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


#Operaciones con sets
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

#Unión de sets
#union= set_a.union(set_b) #Usando metodo union()
union = set_a | set_b #Usando operador | para unión
print("Unión de set_a y set_b:", union) #Nos da todos los elementos de ambos sets, sin duplicados

#Intersección de sets
#interseccion = set_a.intersection(set_b) #Usando metodo intersection()
interseccion = set_a & set_b #Usando operador & para intersección
print("Intersección de set_a y set_b:", interseccion) #Solo nos da los elementos que están en ambos sets

#Diferencia de sets
#diferencia = set_a.difference(set_b) #Usando metodo difference()
diferencia = set_a - set_b #Usando operador - para diferencia
print("Diferencia de set_a y set_b:", diferencia) #Nos da los elementos que están en set_a pero no en set_b
