# CALCULO DE DOMINGOS EN FUNCIÓN AL AÑO
## Parte 1 ("Variables")

**dia_actual = 0**

    0 = Lunes / 1 = Martes / 2 = Miercoles / 3 = Jueves / 4 =  Viernes / 5 = Sabado / 6 = Domingo

**dias_del_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]**

    Solamente varia Febrero, cambiando de 28 a 29 días

**cumplido = 0**

    Funciona para guardar los domingos que cayeron en el primer dia del mes

## Parte 2 ("Inicio del ciclo")

**for año_final in range (1900, 2001):**
    
    Sirve para indicar la los años en los cuales se calculara, tomando en cuenta que este tomara al primer dia del año como Lunes

Posteriormente se toma al año actual y se le asigna que febrero vale 28, para posterior, mediante formulas se descarta que sea un año bisiesto

    dias_del_mes[1] = 28

    if año_final % 4 == 0:
        dias_del_mes[1] = 29

    if año_final % 100 == 0:
        dias_del_mes[1] = 28

    if año_final % 400 == 0:
        dias_del_mes[1] = 29

## Parte 2 ("Calculadora de domingos")

Posterior a esto, una vez conociendo si el año tiene 366 o 365 dias se crea una variable para que empieze en funcion a los dias del mes guardados en su caja.

 por lo que posterior se calculara el dia actual si es igual al "dia" que buscamos contar, en este caso **Domingo = 6** y guardara un valor en la variable indicadora

 Sea o no, posteriormente se hara la formula que nos dira en que dia cae el sigtuiente mes, **ejemplo:** 

 (0 + 31) % 7 = 3  // 3 = Jueves


    for elementos in dias_del_mes:
        if dia_actual == 6:
            cumplido = cumplido + 1
        
        dia_actual = (dia_actual + elementos) % 7

Finalmente se imprime el total de días en los cuales cayeron a principío de mes

    print("Domingos que cayeron en el primer dia del mes desde 1900, hasta 2000: ", cumplido)