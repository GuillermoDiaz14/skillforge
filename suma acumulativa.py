MAXIMO= 5
numero= 1
acumulador= 0

while numero <= MAXIMO:
    print( "Acumulador =",acumulador,"+","numero =",numero)
    acumulador += numero
    numero += 1
print("La suma acumulada es: ", acumulador) 