 #Slicig
#texto [inicio : fin : paso]
texto="programacion"
#Debe de mostrar de la r en adelante por que no estoy indicando el final ni tampoco el paso
print(texto[1:])
#Debe de mostrar de la r en adelante pero ahora el paso va de dos en dos y no de uno en uno como lo hace por default
print(texto[1::2])
#Podemos usar indices negativos , la ultima letra es -1 y de ahi va avanzando haca tras en negativo -2, -3, -4 y asi...
print(texto[-6::])
#Podemos invertir la palabra si colocamos el paso en negativo-

print(texto[::-1])