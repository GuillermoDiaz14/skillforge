#Definicion de una clase en python

class Persona:
    
    def inicializar_persona(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    
    def imprimir_persona(self):
        print("Nombre:",self.nombre)
        print("Edad:",self.edad)

#Programa principal
#Creamos un objeto vacio de la clase Persona
if __name__ == "__main__":#Solo se ejecuta si se ejecuta el archivo principal y no se importa como modulo funciona para pruebas
    #Creamos un objeto vacio de la clase Persona
    persona1 = Persona()

    persona1.inicializar_persona("Jose",23)
    persona1.imprimir_persona()

    #Creamos un objeto vacio de la clase Person
    persona2 = Persona()

    
    persona2.inicializar_persona("Guillermo",32)
    persona2.imprimir_persona()
