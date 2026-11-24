# Gestor de Gastos Personales (Consola)

Aplicación de línea de comandos en Python para registrar, consultar, filtrar y analizar gastos diarios sin necesidad de instalar librerías externas.

---

## ¿Cómo guarda la información el programa?

El programa utiliza dos estructuras principales:
1. **Una lista general (gastos = []):** Funciona como una caja donde se almacenan todos los registros en memoria mientras el programa está abierto.
2. **Diccionarios individuales (nuevo_gasto = {...}):** Cada gasto se guarda como una ficha con tres etiquetas: `"descripcion"`, `"monto"` y `"categoria"`.

---

## Funcionamiento bloque a bloque

### Menú Principal (while True y try/except)
* Mantiene el programa activo en un ciclo continuo hasta que el usuario decida salir.
* Utiliza `try/except ValueError` para atrapar entradas inválidas y evitar que el programa se cierre con error si se escriben letras en lugar de números.

### Bloque 1: Registrar un gasto
* Solicita la **descripción** del gasto y el **monto** en formato decimal (`float`).
* Verifica que el monto sea estrictamente mayor a `0`.
* Permite seleccionar una categoría del `1` al `5` (`Almuerzo`, `Comida`, `Cena`, `Transporte`, `Ocio`).
* Guarda los tres datos en un diccionario y lo añade a la lista `gastos` mediante `.append()`.

### Bloque 2: Listar todos los gastos
* Verifica con `len(gastos) == 0` si la lista está vacía para mostrar un aviso.
* Si existen registros, recorre la lista con un ciclo `for gasto in gastos:`, numera cada elemento (`1, 2, 3...`) e imprime sus valores separados mediante *f-strings*.

### Bloque 3: Filtrar por categoría
* Solicita el nombre de una categoría y lo convierte a minúsculas con `.lower()` para que la búsqueda funcione sin importar si se escribe en mayúsculas o minúsculas.
* Recorre la lista `gastos` con un ciclo `for` y compara cada categoría con la búsqueda del usuario.
* Utiliza un contador (`encontrados`) para avisar al final si no hubo coincidencias.

### Bloque 4: Ver resumen financiero
* Mediante cada vez que se ingreso en el bloque 1 un "monto" fue guardandolo en la variable `acumulado`

### Bloque 5: Salir
* Muestra un mensaje de despedida y detiene la ejecución del programa.

