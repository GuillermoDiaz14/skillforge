#Ejercicio con operadores
nombre_ususario=input("Ingrese su nombre de usuario: ")
pasos= int(input("Ingrese la cantidad de pasos que ha dado: "))

META_PASOS=10000
CALORIAS_POR_PASO=0.04

calorias_quemadas= pasos*CALORIAS_POR_PASO
print(f"Calorías quemadas: {calorias_quemadas}")

if pasos >= META_PASOS:
    print("¡Felicidades! Has alcanzado la meta de pasos.")
else:
    pasos_faltantes = META_PASOS - pasos
    print(f"Te faltan {pasos_faltantes} pasos para alcanzar la meta.")  
