class Persona:

    #Constructor de la clase Persona
    def __init__(self,nombre,apellido,edad):
        #Atributos de la clase Persona
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad

    def mostrar_persona(self):
        print("Nombre:",self.nombre)
        print("Edad:",self.edad)

    #Creacion de objetos
    if __name__=="__main__":
        persona1 = Persona("Jose","Diaz",23)
        persona1.mostrar_persona()
