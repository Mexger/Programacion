dia_actual = 0
dias_del_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
cumplido = 0

for año_final in range (1900, 2001):  ##Calcular entre el tiempo 1900 al 2000
   
    dias_del_mes[1] = 28

    if año_final % 4 == 0:
        dias_del_mes[1] = 29

    if año_final % 100 == 0:
        dias_del_mes[1] = 28

    if año_final % 400 == 0:
        dias_del_mes[1] = 29

    for elementos in dias_del_mes:
        if dia_actual == 6:
            cumplido = cumplido + 1
        
        dia_actual = (dia_actual + elementos) % 7


print("Domingos que cayeron en el primer dia del mes desde 1900, hasta 2000: ", cumplido)