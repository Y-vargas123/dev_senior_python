import datetime

listaExperimentos = []


def agregar_Expermiento():
    """permite un nuevo experimento"""
    print("HOLA, AGREGUE SU NUEVO EXPERIMENTO")
    nombre = input("Escriba el nombre del experimento")
    fecha_Experimento =input("Escriba la fecha del experimento con el siguinete formato DD/MM/AAAA")
    tipo_Experimento =input("Escriba el tipo de experimento")

    nuevo_experimento= [nombre, fecha_Experimento,tipo_Experimento]
    listaExperimentos.append(nuevo_experimento)
    print(f"el experimento {nombre} ha sido agregado exitosamente")


def visualizar_Experimentos():
    
    if not listaExperimentos:
        print("No hay experimentos para mostrar.")
        return
    for exp in listaExperimentos:
        print(f"Nombre: {exp[0]}")
        print(f"Fecha: {exp[1]}")
        print(f"Resultado: {exp[2]}")
        print("-----------------------------")


def eliminar_experimento():
    nombre = input("Ingrese el nombre del experimento a eliminar: ")
    
    for exp in listaExperimentos:
        if exp[0].lower() == nombre.lower():
            listaExperimentos.remove(exp)
            print(f"El experimento '{nombre}' ha sido eliminado.\n")
            return
    print(f"El experimento '{nombre}' no se encontró.\n")

def calcular_estadisticas():
    if not listaExperimentos:
        print("No hay experimentos registrados para mostrar estadísticas.\n")
        return
    
    promedios = [sum(exp[3]) / len(exp[3]) for exp in listaExperimentos]
    maximos = [max(exp[3]) for exp in listaExperimentos]
    minimos = [min(exp[3]) for exp in listaExperimentos]

    print(f"Promedio general de todos los experimentos: {sum(promedios) / len(promedios)}")
    print(f"Máximo general de todos los experimentos: {max(maximos)}")
    print(f"Mínimo general de todos los experimentos: {min(minimos)}\n")



def comprar_experimentos():
    global listaExperimentos

    if not listaExperimentos:
        print("No hay más experimentos disponibles.") #Comprobación de lista vacía
        return
    
    #Mostrar los experimentos disponibles
    print("Experimentos disponibles para comprar:")
    for i, experimento in enumerate(listaExperimentos):
        print(f"{i + 1}. Nombre: {experimento[0]}, Fecha: {experimento[1]}, Tipo: {experimento[2]}") #cada experimento es una lista

    #Si es válida, se "compra" el experimento eliminándolo de la lista y muestra un mensaje.
    try:
         opcion = int(input("Seleccione el número del experimento que desea comprar: ")) 
         if 0<= opcion < len(listaExperimentos):
             comprado= listaExperimentos.pop(opcion)
             print("has comprado el experimento{0}")

         else:
            print("opcion no es valida, seleccione una opcion",(listaExperimentos))

    #Si la opción no es válida o el usuario ingresa un dato incorrecto, se muestra un mensaje de error.
    except ValueError:
        print("entrada no valida, coloque un numero entero")

def generar_informe():
    if not listaExperimentos:
        print("No hay experimentos registrados para generar un informe.\n")
        return
    
    with open("informe_experimentos.txt", "w") as file:
        for exp in listaExperimentos:
            file.write(f"Experimento: {exp[0]} - Fecha: {exp[1]}\n")
            file.write(f"  Tipo: {exp['tipo']}\n")
            file.write(f"  Resultados: {exp[2]}\n")
            file.write(f"  Promedio: {sum(exp[2]) / len(exp[2])}\n")
            file.write(f"  Máximo: {max(exp[2])}\n")
            file.write(f"  Mínimo: {min(exp[2])}\n\n")
    
    print("Informe generado correctamente en 'informe_experimentos.txt'.\n")

def mostrar_menu():
   
   while True:  # Este bucle permite que el menú se muestre repetidamente hasta que el usuario elija salir
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

