#Ejercicio para la demostracion de uso de sets en Python

#Se crea un set para alojar los suscriptores
suscriptores = set()
op= False

while not op:
    print("\nOpción 1: Agregar suscriptor")
    print("Opción 2: Consultar suscriptores")
    print("Opción 3: Eliminar suscriptor")
    print("Opción 4: Salir")
    opcion = input("Seleccione una opción: \n")
    if opcion == "1":
        suscriptores_temporal = set()  # Crear un set temporal para almacenar los suscriptores agregados
        suscriptores_temporal.clear()  # Limpiar el set temporal antes de agregar nuevos suscriptores
        num= input ("Cuantos suscriptores desea agregar?")
        i = 0
        while i < int(num):
            nuevo_suscriptor = input("Ingrese el nombre del nuevo suscriptor: ")
            if nuevo_suscriptor in suscriptores:
                print("El suscriptor ya está en la lista.")
            else:
                suscriptores.add(nuevo_suscriptor)
                suscriptores_temporal = suscriptores.copy()  # Crear una copia temporal del set
                i += 1
            
                print(f"El suscriptor {nuevo_suscriptor} ha sido agregado.")
        print(f"se agregaron correctamente {num} suscriptores a la lista.")
        print("Lista de suscriptores que se agregaron: ", suscriptores_temporal)   
    elif opcion == "2":
        if not suscriptores:
            print("No hay suscriptores en la lista.")
        else:    
            print("Lista de suscriptores: ", suscriptores)
    elif opcion == "3":
        suscriptor_a_eliminar = input("Ingrese el nombre del suscriptor a eliminar: ")
        if suscriptor_a_eliminar in suscriptores:
            suscriptores.remove(suscriptor_a_eliminar)
            print("El suscriptor ha sido eliminado.")
        else:
            print("El suscriptor no está en la lista.")
    elif opcion == "4":
        op = True
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

print("Gracias por usar el sistema de suscriptores.")   