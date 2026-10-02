print("++++++++++++Sistema de entrada de datos++++++++++++")
nombre= input("Escribe tu nombre:")
edad= int(input("Escribe tu edad:"))
salario= float(input("Escribe tu salario:"))
es_jefe= input("¿Eres jefe? (si/no):")

#Vamos a convertir a un tipo boolean la respuesta de si es jefe o no
if es_jefe.lower() == "si":
    es_jefe = True
else:
    es_jefe = False
print("++++++++++++Datos ingresados++++++++++++")
print("Nombre:", nombre)
print("Edad:", edad)
print("Salario:", salario)
print(f"Es jefe: {es_jefe}")