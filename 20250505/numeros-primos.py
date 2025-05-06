# Ejercicio: Definir una lista de 1..1000 y determinen todos los numeros primos que aparecen
# entre el 1 y el 1000, y guardarlos en una lista llamada numeros_primos.

# Resolucion:

numeros = list(range(1,1001))
numeros_primos = []

for num in range(2, len(numeros)+1):
    numPrimo = True
    for i in range(2, num):
        if num%i == 0:
            numPrimo = False
    if numPrimo == True:
        numeros_primos.append(num)
        
print(numeros_primos)