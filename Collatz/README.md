# SECUENCIA DE COLLATZ

El objetivo es demostrar la famosa formula de collatz

## Parte 1 ("Variables")

max_terminos = 0

    Sirve para indicar la cantidad que logro el numero del record

mejor_numero = 0

    Sirve para indicar el numero que logro el record

## Parte 2 ("Inicio del ciclo")

El ciclo for indica desde que cantidad se empezara a buscar el mayor número

Primeramente se vacia una caja y se crea una variable para guardar el número actual: Posterior s ehace la formula para que el nuero actual si es distinto a uno se divida entre dos si es divisible entre este, en otro caso se multiplicara por 3 y se le sumara uno

    for inicio in range(1, 1000000):
    caja = []
    numero = inicio
    while numero != 1:
        caja.append(numero)
        if numero % 2 == 0:
            numero //= 2
        else:
            numero = (numero * 3) + 1
    else:
        caja.append(numero)


## Parte 3 ("Prueba")

Posteriormente se comparara si el numero actual logro superar el numero de terminos del actual "Rey" y si es asi se guardara en las variables de afuera

    if len(caja) > max_terminos:
        max_terminos = len(caja)
        mejor_numero = inicio

Posteriormente una vez realizado todos los calculos, pasara a imprimirse el numero ganador junto con la cantidad que alcanzo

     print("El número inicial con la cadena más larga es:", mejor_numero)
     print("La cantidad de términos de esa cadena es:", max_terminos)