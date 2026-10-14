

#Ejemplo if elif else
edad=11
if edad >18:
    print("Eres mayor de edad tienes", edad, "años")
elif edad >12 and edad <18:
    print("Eres adolescente tienes", edad, "años")
else:
    print("Eres un niño tienes", edad, "años")  

#Ejemplo de sentencias if anidadas

precio=float(input("Ingrese el monto de la compra: "))
es_cliente=input("¿Es cliente? (si/no): ")
if precio > 1000 and es_cliente.lower().strip() == "si":
    print("Tiene un descuento del 10%")
elif es_cliente.lower().strip() == "si" and precio < 1000:
    print("Tiene un descuento del 5%")
else:
    print("No tiene descuento")

#Sentencia invertida
print("Bienvenido al sistema bancario")
salir=input("¿Desea salir del sistema? (si/no): ")

if not salir.lower().strip() == "si":
    print("Gracias por usar el sistema bancario")
else:
    print("Saliendo del sistema bancario")