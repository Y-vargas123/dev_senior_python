import datetime
import os # par vere el archivo donde se guardará el informe

# Lista global de experimentos
listaExperimentos = []

def agregar_Expermiento():
    """Permite agregar un nuevo experimento"""
    print("\n--- AGREGAR NUEVO EXPERIMENTO ---\n")
    nombre = input("Escriba el nombre del experimento: ")
    fecha_Experimento = input("Escriba la fecha del experimento con el siguiente formato DD/MM/AAAA: ")
    tipo_Experimento = input("Escriba el tipo de experimento: ")

    resultados_input = input(f"Ingrese los resultados para el experimento '{nombre}' separados por comas: ")

    try:
        resultados = [float(x.strip()) for x in resultados_input.split(",")]
    except ValueError:
        print("Hubo un error al convertir los resultados. Asegúrese de ingresar solo números separados por comas.\n")
        return

    nuevo_experimento = [nombre, fecha_Experimento, tipo_Experimento, resultados]
    listaExperimentos.append(nuevo_experimento)
    print(f"\nEl experimento '{nombre}' ha sido agregado exitosamente.\n")

def visualizar_Experimentos():
    """Muestra los experimentos guardados"""
    if not listaExperimentos:
        print("\nNo hay experimentos registrados para mostrar.\n")
        return
    print("\n--- EXPERIMENTOS REGISTRADOS ---\n")
    for exp in listaExperimentos:
        print(f"Nombre: {exp[0]}")
        print(f"Fecha: {exp[1]}")
        print(f"Tipo: {exp[2]}")
        print(f"Resultados: {exp[3]}")
        print("-----------------------------\n")

def eliminar_experimento():
    """Permite eliminar un experimento por su nombre"""
    nombre = input("\nIngrese el nombre del experimento a eliminar: ")
    for exp in listaExperimentos:
        if exp[0].lower() == nombre.lower():
            listaExperimentos.remove(exp)
            print(f"\nEl experimento '{nombre}' ha sido eliminado.\n")
            return
    print(f"\nEl experimento '{nombre}' no se encontró.\n")

def calcular_estadisticas():
    """Calcula estadísticas como el promedio, máximo y mínimo de los resultados"""
    if not listaExperimentos:
        print("\nNo hay experimentos registrados para mostrar estadísticas.\n")
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
    
    if promedios:
        print(f"\nPromedio general de todos los experimentos: {sum(promedios) / len(promedios)}")
    else:
        print("\nNo hay resultados para calcular el promedio.")
    
    print(f"\nMáximo general de todos los experimentos: {max(maximos) if maximos else 0}")
    print(f"Mínimo general de todos los experimentos: {min(minimos) if minimos else 0}\n")

def comprar_experimentos():
    """Permite comprar (eliminar) un experimento de la lista"""
    global listaExperimentos

    if not listaExperimentos:
        print("\nNo hay más experimentos disponibles para comprar.\n")  # Comprobación de lista vacía
        return
    
    print("\n--- EXPERIMENTOS DISPONIBLES PARA COMPRAR ---\n")
    for i, experimento in enumerate(listaExperimentos):
        print(f"{i + 1}. Nombre: {experimento[0]}, Fecha: {experimento[1]}, Tipo: {experimento[2]}")

    try:
        opcion = int(input("\nSeleccione el número del experimento que desea comprar: ")) 
        if 0 <= opcion - 1 < len(listaExperimentos):
            comprado = listaExperimentos.pop(opcion - 1)
            print(f"\nHas comprado el experimento: {comprado[0]}\n")
        else:
            print("\nOpción no válida, seleccione una opción válida.\n")

    except ValueError:
        print("\nEntrada no válida, coloque un número entero.\n")

def generar_informe():
    """Genera un informe con los experimentos y estadísticas generales"""
    if not listaExperimentos:
        print("\nNo hay experimentos registrados para generar un informe.\n")
        return
    
    directorio_actual = os.getcwd()
    archivo_informe = os.path.join(directorio_actual, "informe_experimentos.txt")

    with open(archivo_informe, "w") as file:
        file.write("----- Informe de Experimentos -----\n\n")
        file.write("Descripción de los experimentos:\n")
        for exp in listaExperimentos:
            file.write(f"\nNombre: {exp[0]}\n")
            file.write(f"Fecha: {exp[1]}\n")
            file.write(f"Tipo: {exp[2]}\n")
            file.write(f"Resultados: {exp[3]}\n")
            file.write(f"Promedio: {sum(exp[3]) / len(exp[3]) if exp[3] else 0}\n")
            file.write(f"Máximo: {max(exp[3]) if exp[3] else 0}\n")
            file.write(f"Mínimo: {min(exp[3]) if exp[3] else 0}\n")
            file.write("-----------------------------\n")
        
        file.write("\n===== Análisis Estadístico General =====\n")
        if listaExperimentos:
            promedios = [sum(exp[3]) / len(exp[3]) for exp in listaExperimentos if exp[3]]
            maximos = [max(exp[3]) for exp in listaExperimentos if exp[3]]
            minimos = [min(exp[3]) for exp in listaExperimentos if exp[3]]

            file.write(f"Promedio general de todos los experimentos: {sum(promedios) / len(promedios) if promedios else 0}\n")
            file.write(f"Máximo general de todos los experimentos: {max(maximos) if maximos else 0}\n")
            file.write(f"Mínimo general de todos los experimentos: {min(minimos) if minimos else 0}\n")

        file.write("\n===== Conclusión =====\n")
        if promedios:
            promedio_general = sum(promedios) / len(promedios)
            if promedio_general > 10:
                file.write("Los experimentos muestran resultados generalmente altos.\n")
            elif promedio_general < 5:
                file.write("Los experimentos muestran resultados generalmente bajos.\n")
            else:
                file.write("Los experimentos muestran resultados equilibrados.\n")
        else:
            file.write("No hay resultados suficientes para generar una conclusión.\n")
        
    print(f"\nInforme generado correctamente en '{archivo_informe}'.\n")

def comparar_experimentos():
    """Compara los experimentos basándose en el criterio seleccionado"""
    if not listaExperimentos:
        print("\nNo hay experimentos registrados para comparar.\n")
        return

    print("\nSeleccione el criterio para comparar los experimentos:")
    print("1. Promedio de los resultados")
    print("2. Máximo de los resultados")
    print("3. Mínimo de los resultados")
    
    try:
        criterio = int(input("\nIngrese el número del criterio (1-3): "))
        
        if criterio == 1:
            listaOrdenada = sorted(listaExperimentos, key=lambda exp: sum(exp[3]) / len(exp[3]) if exp[3] else 0, reverse=True)
            print("\n--- EXPERIMENTOS ORDENADOS POR PROMEDIO ---\n")
        elif criterio == 2:
            listaOrdenada = sorted(listaExperimentos, key=lambda exp: max(exp[3]) if exp[3] else 0, reverse=True)
            print("\n--- EXPERIMENTOS ORDENADOS POR MÁXIMO ---\n")
        elif criterio == 3:
            listaOrdenada = sorted(listaExperimentos, key=lambda exp: min(exp[3]) if exp[3] else 0, reverse=True)
            print("\n--- EXPERIMENTOS ORDENADOS POR MÍNIMO ---\n")
        else:
            print("\nOpción no válida.\n")
            return

        for exp in listaOrdenada:
            promedio = sum(exp[3]) / len(exp[3]) if exp[3] else 0
            max_resultado = max(exp[3]) if exp[3] else 0
            min_resultado = min(exp[3]) if exp[3] else 0
            print(f"\nNombre: {exp[0]}")
            print(f"Fecha: {exp[1]}")
            print(f"Tipo: {exp[2]}")
            print(f"Resultados: {exp[3]}")
            print(f"Promedio: {promedio}")
            print(f"Máximo: {max_resultado}")
            print(f"Mínimo: {min_resultado}")
            print("-----------------------------\n")

    except ValueError:
        print("\nEntrada no válida, por favor ingrese un número entero entre 1 y 3.\n")

def mostrar_menu():
    """Muestra el menú principal y maneja las opciones"""
    while True:
        print("\n--- MENÚ PRINCIPAL ---\n")
        print("1. Agregar Experimento")
        print("2. Visualizar Experimentos")
        print("3. Eliminar Experimento")
        print("\n===== Análisis de Datos =====")
        print("4. Calcular Estadísticas")
        print("5. Comprar Experimentos")
        print("6. Generar Informes")
        print("7. Comparar Experimentos")
        print("\n8. Salir")

        try:
            opcion = int(input("\nSeleccione una opción (1-8): "))
            
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
                comparar_experimentos()
            elif opcion == 8:
                print("\n¡Gracias por usar el programa!\n")
                break  
            else:
                print("\nOpción no válida. Por favor, elija un número entre 1 y 8.\n")
        except ValueError:
            print("\nEntrada no válida. Por favor, ingrese un número entero.\n")

if __name__ == "__main__":
    mostrar_menu()
