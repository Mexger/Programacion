# SUMA DE NUMEROS PRIMOS

## Parte 1 ("Variables")

     suma = 0

Es el contador que indica cuantos numeros son primos, sumandose mientras cada número primo aparecia

## Parte 2 ("Formula")

El ciclo for inicial revisa todos los números que hay dentro de la cantidad seleccionada, y se incluye un reinicio a la variante divisora.

El segundo for sirve para comprobar si el numero es primo, para esto se divide por multiplicandolo por su raiz y sumandole uno, so es par, se rompe e intenta con el siguiente numero, en caso de que ningun numero pudiese dividirlo lo suma a la variable de "suma" para guardarlo.

    for numero in range (2, 2000000):
    divisor= 0
    for x in range(2, int(numero**0.5) + 1):
        if numero % x == 0: 
            divisor= divisor + 1
            break
    if divisor == 0:
        suma= suma + numero 

Posteriormente, una vez calculado todos los numeros primos, se imprimira.

    print("tu número sumado es:", suma)