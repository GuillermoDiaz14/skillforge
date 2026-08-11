#Uso de replace en python
texto=("Hello World, how are you? Hello World, how are you? Hello World, "
       "how are you? Hello World, how are you?")

#Vamos a reemplazar world por python
nuevo = texto.replace("World","python")
print(texto)

print(nuevo)

#Vamos a reemplazar world por python solo 2 veces
nuevo = texto.replace("World","python",2)
print(nuevo)