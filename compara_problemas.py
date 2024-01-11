# Importa el módulo os para trabajar con funcionalidades del sistema operativo
import os

def compareTriplets(a, b):
    # Función para comparar las puntuaciones finales

    # Inicialización de las puntuaciones de Lucia y Carlos
    puntuacion_lucia = 0
    puntuacion_carlos = 0

    # Iteración sobre las tres categorías
    for i in range(3):
        # Comparación de las puntuaciones en cada categoría y actualización de los puntajes
        if a[i] > b[i]:
            puntuacion_lucia += 1
        elif a[i] < b[i]:
            puntuacion_carlos += 1
    
    # Devuelve una lista con las puntuaciones finales
    return [puntuacion_lucia, puntuacion_carlos]

# Bloque principal del programa
if __name__ == "__main__":
    # Utiliza el módulo os para obtener la ruta del directorio actual
    directorio_actual = os.path.dirname(os.path.realpath(__file__))
    
    # Combina la ruta del directorio actual con el nombre del archivo de salida
    ruta_resultados = os.path.join(directorio_actual, 'resultados.txt')

    # Abre el archivo de salida en modo escritura
    fptr = open(ruta_resultados, 'w')

    # Título para la sección de comparación de problemas
    titulo = "COMPARACIÓN DE PROBLEMAS"
    print("\n" + titulo + "\n" + "-" * len(titulo))

    # Información sobre la tarea a realizar      
    print(
        "\nLucía y Carlos han creado un problema cada uno que serán evaluados en tres categorías: claridad, originalidad y dificultad."
        "\nTu tarea es asignar puntuaciones del 1 al 100 a cada categoría."
        "\nDespués de evaluar ambos problemas, recibirás un archivo llamado 'resultados.txt' que mostrará cuántas categorías ha ganado cada uno." 
        "\nLa victoria en una categoría requiere una puntuación superior al oponente, en caso de empate, ninguno suma puntos en esa categoría."
        )
    
    # Solicita la entrada de puntuaciones para Lucía
    while True:
        try:
            a = list(map(int, input("\nIngresa la puntuación de Lucía de cada categoría separada por espacios (ej: 60 25 73): ").rstrip().split()))

            if all(0 <= puntuacion <= 100 for puntuacion in a) and len(a) == 3:
                break
            else:
                print("\nPor favor, ingresa tres números entre 0 y 100")
        except ValueError:
            print("\nPor favor, ingresa números válidos.")

    # Solicita la entrada de puntuaciones para Carlos
    while True:
        try:
            b = list(map(int, input("\nIngresa la puntuación de Carlos de cada categoría separada por espacios (ej: 40 85 21): ").rstrip().split()))

            if all(0 <= puntuacion <= 100 for puntuacion in b) and len(b) == 3:
                break
            else:
                print("\nPor favor, ingresa tres números entre 0 y 100")
        except ValueError:
            print("\nPor favor, ingresa números válidos.")

    # Calcula el resultado de la comparación de puntuaciones
    resultado = compareTriplets(a, b)

    # Título para la sección de resultados en el archivo de salida
    titulo_resultados = "Resultados"
    fptr.write(titulo_resultados + "\n" + "-" * len(titulo_resultados))
    fptr.write("\n")

    # Escribe las categorías ganadas por Lucía y Carlos en el archivo de salida
    fptr.write("\nCategorias ganadas por Lucia vs Carlos")
    fptr.write("\n")
    fptr.write(f"{resultado[0]} vs {resultado[1]}")

    # Determina al ganador y escribe la información en el archivo de salida
    if resultado[0] > resultado[1]:
        fptr.write("\nGanador: Lucia")
    elif resultado[0] < resultado[1]:
        fptr.write("\nGanador: Carlos")
    else:
        fptr.write("\nEmpate: No hay un ganador")

    # Cierra el archivo de salida
    fptr.close()