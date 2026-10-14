print("**** Lista de reproducción ****")

lista_reproduccion = []

# Agregar canciones a la lista de reproducción
lista_reproduccion.append("Canción 4 - Artista D")
lista_reproduccion.append("Canción 5 - Artista E")
lista_reproduccion.append("Canción 1 - Artista A")
lista_reproduccion.append("Canción 2 - Artista B")
lista_reproduccion.append("Canción 3 - Artista C")

print("Lista de reproducción actual:")
for cancion in lista_reproduccion:
    print(cancion)

# Mostrar la lista de reproducción en orden alfabético
lista_reproduccion.sort()
print("\nLista de reproducción en orden alfabético:")
for cancion in lista_reproduccion:
    print(cancion)

# Mostrar la lista de reproducción en orden alfabético  inverso
lista_reproduccion.sort(reverse=True)
print("\nLista de reproducción en orden alfabético inverso:")
for cancion in lista_reproduccion:
    print(cancion)

cantidad_canciones = int(input("\nIngrese la cantidad de canciones que desea agregar a la lista de reproducción: "))

for _ in range(cantidad_canciones):
    cancion = input("Ingrese el nombre de la canción: ")
    artista = input("Ingrese el nombre del artista: ")
    lista_reproduccion.append(f"{cancion} - {artista}")

print("\nLista de reproducción actual:")
for cancion in lista_reproduccion:
    print(cancion)