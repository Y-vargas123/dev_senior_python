import datetime

listaExperimentos = []

def agregar_experimento():
    print("HOLA, AGREGUE SU NUEVO EXPERIMENTO")
    
    nombre = input("Escriba el nombre del experimento: ")
    
    while True:
        try:
            fecha_Experimento = input("Escriba la fecha del experimento con el siguiente formato DD/MM/AAAA: ")
            datetime.datetime.strptime(fecha_Experimento, "%d/%m/%Y")
            break
        except ValueError:
            print("Fecha inválida. Por favor ingrese la fecha en el formato DD/MM/AAAA.")
    
    tipo_Experimento = input("Escriba el tipo de experimento: ")
    
    while True:
        try:
            resultados = list(map(float, input("Ingrese los resultados del experimento separados por comas: ").split(',')))
            break
        except ValueError:
            print("Por favor ingrese solo números para los resultados.")
    
    nuevo_experimento = {
        'nombre': nombre,
        'fecha': fecha_Experimento,
        'tipo': tipo_Experimento,
        'resultados': resultados
    }
    
    listaExperimentos.append(nuevo_experimento)
    print(f"El experimento '{nombre}' ha sido agregado exitosamente.\n")

def visualizar_experimentos():
    if not listaExperimentos:
        print("No hay experimentos para mostrar.\n")
        return
    
    for exp in listaExperimentos:
        print(f"Nombre: {exp['nombre']}")
        print(f"Fecha: {exp['fecha']}")
        print(f"Tipo: {exp['tipo']}")
        print(f"Resultados: {exp['resultados']}")
        print(f"Promedio: {sum(exp['resultados']) / len(exp['resultados'])}")
        print(f"Máximo: {max(exp['resultados'])}")
        print(f"Mínimo: {min(exp['resultados'])}")
        print("-----------------------------")

def eliminar_experimento():
    nombre = input("Ingrese el nombre del experimento a eliminar: ")
    
    for exp in listaExperimentos:
        if exp['nombre'].lower() == nombre.lower():
            listaExperimentos.remove(exp)
            print(f"El experimento '{nombre}' ha sido eliminado.\n")
            return
    print(f"El experimento '{nombre}' no se encontró.\n")

def calcular_estadisticas():
    if not listaExperimentos:
        print("No hay experimentos registrados para mostrar estadísticas.\n")
        return
    
    promedios = [sum(exp['resultados']) / len(exp['resultados']) for exp in listaExperimentos]
    maximos = [max(exp['resultados']) for exp in listaExperimentos]
    minimos = [min(exp['resultados']) for exp in listaExperimentos]

    print(f"Promedio general de todos los experimentos: {sum(promedios) / len(promedios)}")
    print(f"Máximo general de todos los experimentos: {max(maximos)}")
    print(f"Mínimo general de todos los experimentos: {min(minimos)}\n")

def generar_informe():
    if not listaExperimentos:
        print("No hay experimentos registrados para generar un informe.\n")
        return
    
    with open("informe_experimentos.txt", "w") as file:
        for exp in listaExperimentos:
            file.write(f"Experimento: {exp['nombre']} - Fecha: {exp['fecha']}\n")
            file.write(f"  Tipo: {exp['tipo']}\n")
            file.write(f"  Resultados: {exp['resultados']}\n")
            file.write(f"  Promedio: {sum(exp['resultados']) / len(exp['resultados'])}\n")
            file.write(f"  Máximo: {max(exp['resultados'])}\n")
            file.write(f"  Mínimo: {min(exp['resultados'])}\n\n")
    
    print("Informe generado correctamente en 'informe_experimentos.txt'.\n")

def menu():
    while True:
        print("---- MENÚ DE GESTIÓN DE EXPERIMENTOS ----")
        print("1. Agregar un nuevo experimento")
        print("2. Ver experimentos registrados")
        print("3. Calcular estadísticas generales")
        print("4. Generar informe")
        print("5. Eliminar un experimento")
        print("6. Salir")
        
        opcion = input("Elige una opción (1-6): ")
        
        if opcion == '1':
            agregar_experimento()
        elif opcion == '2':
            visualizar_experimentos()
        elif opcion == '3':
            calcular_estadisticas()
        elif opcion == '4':
            generar_informe()
        elif opcion == '5':
            eliminar_experimento()
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor elige una opción entre 1 y 6.")

if __name__ == "__main__":
    menu()
