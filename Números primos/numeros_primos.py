suma = 0

for numero in range (2, 2000000):
    divisor= 0
    for x in range(2, int(numero**0.5) + 1):
        if numero % x == 0: ##Comprobamos si el número es divisible por algún número y la raíz cuadrada del número
            divisor= divisor + 1
            break
    if divisor == 0:
        suma= suma + numero 

print("tu número sumado es:", suma)