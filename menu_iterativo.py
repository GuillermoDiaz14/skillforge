#Menu iterativo de Administración de usuarios
print("Bienvenido al sistema de administración de usuarios")
opcion=0
salir=False
while salir != True:
    opcion = input (f"""Opciones disponibles:
      1. Crear usuario
      2. Editar usuario
      3. Eliminar usuario
      4. Salir

      Ingrese el número de la opción que desea seleccionar:
      """)
    if opcion == "1":
        print("Opción 1: Crear usuario\n")
    elif opcion == "2":
        print("Opción 2: Editar usuario\n")
    elif opcion == "3":
        print("Opción 3: Eliminar usuario\n")
    elif opcion == "4":
        salir=True
        print("Gracias por usar el sistema de administración de usuarios. ¡Hasta luego!")
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.\n")
else:
    print("El programa ha finalizado.")