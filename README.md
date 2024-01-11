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