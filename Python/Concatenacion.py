from Python.main import mensaje

nombre = "Guillermo"
edad = 18
pais = "Mexico"
ciudad = "Gdl"
Activo = True

#Concatenacion basica
print("Nombre:¡"+" "+nombre+" "+"pais"+" "+pais)

#f String
presentacion = f"Hola yo soy {nombre} y tengo {edad + 5}, soy de {pais} y vivo en {ciudad}. Activo: {Activo}"
print(presentacion)

#Funcion Len para obtener la logitud
mensaje="Hola mundo"
Tamanio= len(mensaje)
print(f"La longitud es: {Tamanio}")

#Mayusculas y minusculas
texto = " PyThOn"
print(f"mensaje original: {texto}")
print(f"en minusculas {texto.lower()}")
print(f"en mayusculas {texto.upper()}")

#GATO
#[G][A][T][O]
singular= "gato"
plural="gato"+"s"
print(singular)
print(plural)

#tambien podemos hacerlo con llaves y es lo mismo
print(f"usando llaves: {singular}s")


