#!/bin/python3
import math
import os
import random
import re
import sys



def countApplesAndOranges(s, t, a, b, apples, oranges):
        while True:
        
            # Calcula las posiciones de caída de las manzanas y cuenta cuántas caen dentro del rango
            apples_in_range = sum(1 for apple in apples if s <= (a + int(apple)) <= t)

            # Calcula las posiciones de caída de las naranjas y cuenta cuántas caen dentro del rango
            oranges_in_range = sum(
                1 for orange in oranges if s <= (b + int(orange)) <= t
            )

            # Imprime la cantidad de manzanas y naranjas en líneas separadas
            print("Manzanas en la casa de Sam:", apples_in_range)
            print("Naranjas en la casa de Sam:", oranges_in_range)
            break  # Sale del bucle si no hay errores
        


if __name__ == "__main__":

    s = "a"
    t = "a"
    a = "a"
    b = "a"
    m = "a"
    n = "a"
    x = "a"

    while s == "a" or t == "a" or s >= t:
        try:
            print(
                "Ingrese el punto de inicio y final de la ubicación de la casa de Sam, separados por un espacio; ejemplo 3 4 :"
            )
            s, t = map(int, input().split())
        except ValueError:
            s = "a"
            t = "a"
            print(
                "Error: Por favor, asegúrate de ingresar números válidos para todas las entradas."
            )

    while a == "a" or b == "a" or a >= s or b <= t:
        try:
            print("Ingrese la ubicación del manzano y del naranjo; ejemplo: (2 4):")
            a, b = map(int, input().split())
        except ValueError:
            a = "a"
            b = "a"
            print(
                "Error: Por favor, asegúrate de ingresar números válidos para todas las entradas."
            )

    while  m == "a" or n == "a" or m < 0 or n < 0:
        try:
            print("Ingrese la cantidad de manzanas y naranjas (m n):")
            m, n = map(int, input().split())
        except ValueError:
            m = "a"
            n = "a"
            print(
                "Error: Por favor, asegúrate de ingresar números válidos para todas las entradas."
        )
    while x == "a" :
        apples = []
        try:
            print(f"Ingrese las distancias a las que han caído las {m} manzanas separadas por espacios (ten en cuenta que si caen a la izquierda de el arbol se indican con numeros negativos): ")
            apples = list(map(int,input().split()))
        except ValueError:
            x = "a"
            print("Error: Por favor, asegúrate de ingresar números válidos para todas las entradas.")

        if len(apples) != m :
            print(f"Error: Debes ingresar exactamente {m} números separados por espacios.")
            x = "a"
        elif len(apples) == m :
            x = "b"

    while x == "b":
        oranges = []
        try:
            print(f"Ingrese las distancias a las que han caído las {n} naranajas separadas por espacios:")
            oranges = list(map(int,input().split()))
        except ValueError:
            x = "b"
            print("Error: Por favor, asegúrate de ingresar números válidos para todas las entradas.")

        if len(oranges) != n :
            print(f"Error: Debes ingresar exactamente {n} números separados por espacios.")
            x = "b"
        if len(oranges) == n :
            x = "c"

    # Llama a la función countApplesAndOranges con los valores proporcionados por el usuario
    countApplesAndOranges(s, t, a, b, apples, oranges)





