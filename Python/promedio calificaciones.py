num_cal=input("Ingrese el número de calificaciones: ")
lista_calificaciones=[]

for i in range(int(num_cal)):
    calificacion=float(input(f"Ingrese la calificación {i+1}: "))
    lista_calificaciones.append(calificacion)

promedio=sum(lista_calificaciones)/len(lista_calificaciones)
print("El promedio de las calificaciones es:", f"{promedio:.2f}")
3
