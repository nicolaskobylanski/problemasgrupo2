# Comparador de Puntuaciones
Este programa en Python permite comparar las puntuaciones de Lucía y Carlos en tres categorías diferentes: claridad, originalidad y dificultad. El resultado se muestra indicando cuántas categorías ha ganado cada uno.
## Uso
1. Ejecución del Programa:
* Asegúrate de tener Python instalado en tu sistema.
* Ejecuta el script desde la línea de comandos o terminal.
2. Entrada de Puntuaciones:
* Ingresa las puntuaciones de Lucía y Carlos cuando se solicite.
* Cada puntuación debe ser un número entre 0 y 100, y se deben proporcionar tres puntuaciones separadas por espacios.
3. Resultados:
* El programa calculará y mostrará cuántas categorías ha ganado Lucía y cuántas ha ganado Carlos.
* El resultado se guardará en un archivo llamado resultados.txt.
## Estructura del Código
El código consta de una función principal (**'compareTriplets'**) que compara las puntuaciones en tres categorías y devuelve un resultado. También, se utiliza el módulo **'os'** para gestionar rutas de archivos.
## Archivo de Salida ('resultados.txt')
El programa generará un archivo de salida (**'resultados.txt'**) que contiene la comparación de categorías y el ganador.
**Nota:** En caso de empate, se indicará que no hay un ganador.

# Contador de Manzanas y Naranjas
Este script en Python resuelve el problema de contar cuántas manzanas y naranjas caen dentro del rango de una casa. La posición de la casa se define por un punto de inicio (s) y un punto final (t), mientras que los árboles de manzanas (a) y naranjas (b) se ubican en diferentes posiciones.
## Estructura del Código
El código se organiza en funciones para mejorar la legibilidad y modularidad, y también incluye funciones específicas para validar la entrada del usuario. Aquí están las funcionalidades clave del script:
* countApplesAndOranges: Calcula y muestra la cantidad de manzanas y naranjas que caen dentro del rango de la casa de Sam.
* get_valid_input: Solicita al usuario una entrada específica y valida que sea válida según ciertos criterios.
* main: La función principal que guía al usuario a través del proceso de ingreso de datos, asegurando que se proporcionen valores válidos.
## Funcionalidades Adicionales
* Manejo de Errores: El script maneja errores de entrada para garantizar que el usuario ingrese valores válidos en cada paso.
* Validación de Rangos y Cantidades: Se implementan controles para asegurarse de que los valores ingresados cumplan con requisitos específicos, como que el punto de inicio sea menor que el punto final y que la cantidad de frutas sea un número no negativo.
* Flexibilidad con Distancias: El script permite ingresar distancias positivas y negativas para representar caídas a la izquierda o a la derecha de los árboles.
* Modularidad: Las funciones están diseñadas de manera modular, facilitando la expansión y el mantenimiento del código.

# Laberinto de Alef

Este programa simula un laberinto donde Alef, el personaje principal, debe encontrar la salida. El laberinto se representa mediante un tablero, donde Alef comienza en una posición inicial y debe navegar a través de diferentes celdas para llegar a la salida. Algunas celdas pueden contener obstáculos o rutas alternativas.

## Estructura del Código

El código está organizado de la siguiente manera:

- **Entrada de Datos**: El usuario debe proporcionar el número de filas, columnas y túneles en el laberinto. Además, se solicita la estructura del laberinto y las coordenadas de los túneles (entradas y salidas).

- **Definición de Estados y Transiciones**: Se asignan índices a los estados del tablero (celdas accesibles, obstáculos, punto de inicio y salidas). Luego, se construyen las transiciones entre estados, modelando los movimientos posibles de Alef.

- **Iteración de Valor**: Se utiliza el algoritmo de iteración de valor para calcular la probabilidad de llegar a la salida desde el estado inicial.

- **Salida de Resultados**: El programa imprime la probabilidad de que Alef escape del laberinto.

## Cómo Introducir el Input del Usuario

1. **Dimensiones del Laberinto**: Introduzca el número de filas, columnas y túneles en el laberinto, separados por espacios.

    Ejemplo:
    ```
    5 5 2
    ```

2. **Estructura del Laberinto**: Ingrese la estructura del laberinto, especificando las celdas como 'A' (punto de inicio), '%' (salida), 'O' (celda normal), '#' (obstáculo) o '*' (celda mortal).

    Ejemplo:
    ```
    OOOOO
    OAOOO
    OOOOO
    O%OOO
    OOOOO
    ```

3. **Coordenadas de Túneles**: Proporcione las coordenadas de los túneles, indicando la entrada y la salida para cada túnel.

    Ejemplo:
    ```
    2 2 4 5
    4 3 1 1
    ```

4. **Resultados**: El programa imprimirá la probabilidad de que Alef escape del laberinto.

    Ejemplo de Resultado:
    ```
    Esta es la probabilidad de que Alef escape del laberinto: 75.0%
    ```

**Nota**: Siga las instrucciones del programa y asegúrese de ingresar los datos de manera correcta para obtener resultados precisos.

