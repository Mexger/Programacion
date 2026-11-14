suma = 1
caja = []
numero = int(input("Dame un número entero: "))
while numero != 1:
    caja.append(numero)
    if suma < numero:
         suma = numero 
    if numero%2==0:
        numero //= 2
    else:
        numero = (numero * 3)+1

print("La cadena tiene:", len(caja))
print("El número mas largo de la cadena es:", suma)