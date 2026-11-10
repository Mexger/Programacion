suma = 0

for numero in range (2, 2000000):
    divisor= 0
    for x in range(2, int(numero**0.5) + 1): ##LA IA ME DIJO ESTO PARA EVITAR QUE MI PROCESO DURE HORAS, puesto que yo habia puesto un ciclo for que probaba todos los numeros posibles, teniendo 138 mil millones de combinaciones, al contrario de comprobar si tenia raiz cuadrada
        if numero % x == 0:
            divisor= divisor + 1
            break
    if divisor == 0:
        suma= suma + numero 

print("tu número sumado es:", suma)