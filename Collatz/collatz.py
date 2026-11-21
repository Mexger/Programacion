max_terminos = 0
mejor_numero = 0

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

    if len(caja) > max_terminos:
        max_terminos = len(caja)
        mejor_numero = inicio

print("El número inicial con la cadena más larga es:", mejor_numero)
print("La cantidad de términos de esa cadena es:", max_terminos)