import datetime

listaExperimentos = []

def agregar_Expermiento():
    print("HOLA, AGREGUE SU NUEVO EXPERIMENTO")
    nombre = input("Escriba el nombre del experimento: ")
    fecha_Experimento = input("Escriba la fecha del experimento con el siguiente formato DD/MM/AAAA: ")
    tipo_Experimento = input("Escriba el tipo de experimento: ")

    resultados_input = input(f"Ingrese los resultados para el experimento {nombre} separados por comas: ")

    try:
        resultados = [float(x.strip()) for x in resultados_input.split(",")]
    except ValueError:
        print("Hubo un error al convertir los resultados. Asegúrese de ingresar solo números separados por comas.")
        return

    nuevo_experimento = [nombre, fecha_Experimento, tipo_Experimento, resultados]
    listaExperimentos.append(nuevo_experimento)
    print(f"El experimento {nombre} ha sido agregado exitosamente")


def visualizar_Experimentos():
    """Muestra los experimentos guardados"""
    if not listaExperimentos:
        print("No hay experimentos para mostrar.")
        return
    for exp in listaExperimentos:
        print(f"Nombre: {exp[0]}")
        print(f"Fecha: {exp[1]}")
        print(f"Tipo: {exp[2]}")
        print(f"Resultados: {exp[3]}")
        print("-----------------------------")

def eliminar_experimento():
    """Permite eliminar un experimento por su nombre"""
    nombre = input("Ingrese el nombre del experimento a eliminar: ")
    for exp in listaExperimentos:
        if exp[0].lower() == nombre.lower():
            listaExperimentos.remove(exp)
            print(f"El experimento '{nombre}' ha sido eliminado.\n")
            return
    print(f"El experimento '{nombre}' no se encontró.\n")

def calcular_estadisticas():
    """Calcula estadísticas como el promedio, máximo y mínimo de los resultados"""
    if not listaExperimentos:
        print("No hay experimentos registrados para mostrar estadísticas.\n")
        return
    
    promedios = []
    maximos = []
    minimos = []
    
    for exp in listaExperimentos:
        if exp[3]:  # Verificamos si la lista de resultados no está vacía
            promedios.append(sum(exp[3]) / len(exp[3]))
            maximos.append(max(exp[3]))
            minimos.append(min(exp[3]))
        else:
            promedios.append(0)
            maximos.append(0)
            minimos.append(0)
    
    # Si no hay experimentos con resultados, evitamos la división por 0
    if promedios:
        print(f"Promedio general de todos los experimentos: {sum(promedios) / len(promedios)}")
    else:
        print("No hay resultados para calcular el promedio.")
    
    print(f"Máximo general de todos los experimentos: {max(maximos) if maximos else 0}")
    print(f"Mínimo general de todos los experimentos: {min(minimos) if minimos else 0}\n")

def comprar_experimentos():
    """Permite comprar (eliminar) un experimento de la lista"""
    global listaExperimentos

    if not listaExperimentos:
        print("No hay más experimentos disponibles.")  # Comprobación de lista vacía
        return
    
    # Mostrar los experimentos disponibles
    print("Experimentos disponibles para comprar:")
    for i, experimento in enumerate(listaExperimentos):
        print(f"{i + 1}. Nombre: {experimento[0]}, Fecha: {experimento[1]}, Tipo: {experimento[2]}")

    # Si es válida, se "compra" el experimento eliminándolo de la lista
    try:
        opcion = int(input("Seleccione el número del experimento que desea comprar: ")) 
        if 0 <= opcion - 1 < len(listaExperimentos):
            comprado = listaExperimentos.pop(opcion - 1)
            print(f"Has comprado el experimento: {comprado[0]}")

        else:
            print("Opción no válida, seleccione una opción válida.")

    # Si la opción no es válida o el usuario ingresa un dato incorrecto
    except ValueError:
        print("Entrada no válida, coloque un número entero")

def generar_informe():
    """Genera un informe con los detalles de todos los experimentos"""
    if not listaExperimentos:
        print("No hay experimentos registrados para generar un informe.\n")
        return
    
    with open("informe_experimentos.txt", "w") as file:
        for exp in listaExperimentos:
            file.write(f"Experimento: {exp[0]} - Fecha: {exp[1]}\n")
            file.write(f"  Tipo: {exp[2]}\n")
            file.write(f"  Resultados: {exp[3]}\n")
            file.write(f"  Promedio: {sum(exp[3]) / len(exp[3]) if exp[3] else 0}\n")
            file.write(f"  Máximo: {max(exp[3]) if exp[3] else 0}\n")
            file.write(f"  Mínimo: {min(exp[3]) if exp[3] else 0}\n\n")
    
    print("Informe generado correctamente en 'informe_experimentos.txt'.\n")

def mostrar_menu():
    """Muestra el menú principal y maneja las opciones"""
    while True:  # Este bucle permite que el menú se muestre repetidamente
        print("\n--- MENU PRINCIPAL ---")
        print("1. Agregar Experimento")
        print("2. Visualizar Experimentos")
        print("3. Eliminar Experimento")
        print("===== Análisis de Datos =====")
        print("4. Calcular Estadísticas")
        print("5. Comprar Experimentos")
        print("6. Generar Informes")
        print("7. Salir")

        try:
            opcion = int(input("Seleccione una opción (1-7): "))
            
            # Validación de las opciones
            if opcion == 1:
                agregar_Expermiento()
            elif opcion == 2:
                visualizar_Experimentos()
            elif opcion == 3:
                eliminar_experimento()
            elif opcion == 4:
                calcular_estadisticas()
            elif opcion == 5:
                comprar_experimentos()
            elif opcion == 6:
                generar_informe()
            elif opcion == 7:
                print("¡Gracias por usar el programa!")
                break  
            else:
                print("Opción no válida. Por favor, elija un número entre 1 y 7.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")

if __name__ == "__main__":
    mostrar_menu()

