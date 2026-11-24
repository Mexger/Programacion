apartado = 0
monto = 0
continuar = 0
acumulado = 0
gastos = []

while True:
    try:
        apartado = 0
        monto = 0

        print("\n---¿Que desea hacer?--- \n[1] = Registrar un gasto \n[2] = Listar todos los gastos \n[3] = Filtar por categoria \n[4] = Ver total gastado \n[5] = Salirse")
        apartado = int(input("Ingrese el apartado a entrar: "))

        if apartado < 1 or apartado > 5:
            print("\n ERROR.099 No existe ese apartado")
            continue

        if apartado == 1:
            while True:
                try:
                    apartado = 0
                    monto = 0

                    descripcion = input("El gasto fue en: ")
                    monto = float(input("\nIngrese el monto ($) gastado: "))

                    if monto <= 0:
                        print("\n-----ERROR.124 No puedes ingresar una cantidad menor o igual a 0.-----")
                        continue

                    print("\n---El gasto fue en--- \n[1] = Almuerzo \n[2] = Comida \n[3] = Cena \n[4] = Transporte \n[5] = Ocio \n\nIngrese [6] = para salirse")
                    apartado = int(input("Ingrese el apartado a entrar: "))

                    if apartado < 1 or apartado > 6:
                        print("\n-----Error.645 Solo se permiten los números solicitados.-----")
                        continue

                    if apartado == 1:
                        print("Se ha guardado en almuerzo: $", monto)
                        acumulado = acumulado + monto
                        nuevo_gasto = {
                            "descripcion": descripcion,
                            "monto": monto,
                            "categoria": "Almuerzo"
                         }
                        gastos.append(nuevo_gasto)

                    if apartado == 2:
                        print("Se ha guardado en comida: $", monto)
                        acumulado = acumulado + monto
                        nuevo_gasto = {
                            "descripcion": descripcion,
                            "monto": monto,
                            "categoria": "Comida"
                         }
                        gastos.append(nuevo_gasto)

                    if apartado == 3:
                        print("Se ha guardado en cena: $", monto)
                        acumulado = acumulado + monto
                        nuevo_gasto = {
                            "descripcion": descripcion,
                            "monto": monto,
                            "categoria": "Cena"
                         }
                        gastos.append(nuevo_gasto)

                    if apartado == 4:
                        print("Se ha guardado en transporte: $", monto)
                        acumulado = acumulado + monto
                        nuevo_gasto = {
                            "descripcion": descripcion,
                            "monto": monto,
                            "categoria": "Transporte"
                         }
                        gastos.append(nuevo_gasto)

                    if apartado == 5:
                        print("Se ha guardado en ocio: $", monto)
                        acumulado = acumulado + monto
                        nuevo_gasto = {
                            "descripcion": descripcion,
                            "monto": monto,
                            "categoria": "Ocio"
                         }
                        gastos.append(nuevo_gasto)

                    if apartado == 6:
                        break

                    continuar = int(input("[1] = Volver al menu principal = \n[2] = Ingresar una nueva cantidad: "))

                    if continuar == 1:
                        break

                    if continuar == 2:
                        continue

                except ValueError:
                    print("\n-----ERROR.645 Solo se permiten valores numéricos.-----")
                    continue

        if apartado == 2:
            if len(gastos) == 0:
                print("\nAún no tienes gastos registrados.")
            else:
                print("\n--- Lista de todos los gastos ---")
                numero = 1
                for gasto in gastos:
                    print(f"{numero}. {gasto['descripcion']} | Categoría: {gasto['categoria']} | Monto: ${gasto['monto']}")
                    numero = numero + 1

        if apartado == 3:
            if len(gastos) == 0:
                print("\nAún no tienes gastos registrados.")
            else:
                busqueda = input("\nEscribe la categoría a buscar (Almuerzo, Comida, Cena, Transporte, Ocio): ").lower()
                encontrados = 0
                
                print(f"\n--- Gastos en {busqueda} ---")
                for gasto in gastos:

                    if gasto["categoria"].lower() == busqueda:
                        print(f"- {gasto['descripcion']}: ${gasto['monto']}")
                        encontrados = encontrados + 1
                
                if encontrados == 0:
                    print("No se encontraron gastos en esa categoría.")

        if apartado == 4:
            if len(gastos) == 0:
                print("\nNo tienes ningún registro aún.")
            else:
                print(f"\n----Tu total gastado es de {acumulado}----")
                  
        if apartado == 5:
            print("Gracias por usar, nos vemos luego :D")
            quit()

    except ValueError:
        print("\n-----ERROR.645 Solo se permiten valores numéricos.-----")
        continue