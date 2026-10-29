#funciones recursivas son aquellas que se llaman a si mismas
#se usan para resolver problemas que se pueden descomponer en subproblemas
#se usan para resolver problemas que se pueden descomponer en subproblemas
print("******** Funciones recursivas ********")
def factorial(n):
    #condicion de parada o caso base cuando n es 0
    if n == 0:
        return 1
    #llamada recursiva cuando n es mayor que 0
    else:
        return n * factorial(n-1)

#Se llama a la funcion factorial con el argumento 5
print(factorial(5))