print("***Agenda***")

persona = [
    {
"nombre":"Jose",
"apellido":"Diaz",
"edad":23
},
{
"nombre":"Guillermo",
"apellido":"Salinas",
"edad":32
}
]
print("lista: ",persona) 

#Acceder al diccionario desde una lista

print(f"""\nDetalle del primer elemento de la lista
Nombre: {persona[0].get('nombre')}
Apellido: {persona[0].get('apellido')}
Edad: {persona[0].get('edad')}
""")

#Recorrer lo elementos de la lista

