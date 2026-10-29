#Aqui colocamos las funciones para poderlas usar desde cualquier otro archivo
def suma(valor1:int,valor2:int):
    resultado= (valor1 + valor2)
    return resultado

def resta(valor1:int,valor2:int):
    resultado= (valor1 - valor2)
    return resultado

#Prueba 
if __name__ == "__main__" :
    print("Resultado: ",suma(5,10))
    print("Resultado: ",resta(15,10))