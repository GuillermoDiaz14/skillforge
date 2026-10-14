#Asignación simple
numero = 10
texto = "Hola"

#Asignación múltiple
a, b, c = 1, "Hola", 6.99
print("a:", a)
print("b:", b)
print("c:", c)

#Asignación encadenada
x = y = z = 10
print("x:", x)
print("y:", y)
print("z:", z)

#Asignación cruzada
x, y = 10, 20
Print("VALORES INICIALES:")
print("x:", x)
print("y:", y)

x, y = y, x
print("x:", x)
print("y:", y)

#Recibir multiples valores de una entrada de texto
nombre, edad = input("Ingrese su nombre y edad separados por un espacio: ").split()
print("Nombre:", nombre.strip())
print("Edad:", edad.strip())    

#Operador de asignacion compuesto
a = 10
b = 15

print("VALORES INICIALES:", "a:", a, "b:", b)

#Operador de asignación suma
a += b #a= a + b
print("VALOR DE a DESPUÉS DE LA ASIGNACIÓN:", a)    

#Operador de asignación resta
a -= b #a= a - b
print("VALOR DE a DESPUÉS DE LA ASIGNACIÓN:", a)

#Operador de asignación multiplicación
a *= b #a= a * b
print("VALOR DE a DESPUÉS DE LA ASIGNACIÓN:", a)

#Operador de asignación división
a /= b #a= a / b
print("VALOR DE a DESPUÉS DE LA ASIGNACIÓN:", a)

#Operador de asignación división entera
a //= b #a= a // b
print("VALOR DE a DESPUÉS DE LA ASIGNACIÓN:", a)
