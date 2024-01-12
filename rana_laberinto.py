if __name__ == '__main__':
    # Entrada de las dimensiones del tablero y la cantidad de salidas
    print("Introduzca el numero de filas, columnas y túneles en el laberinto (separados por espacios): ")
    filas, columnas, salidas = map(int, input().rstrip().split())

    # Lectura del tablero
    print("Introduzca la estructura del laberinto: ")
    tablero = [list(input()) for _ in range(filas)]
    salidas_dict = dict()  # Diccionario para almacenar las salidas

    # Lectura de las salidas y sus destinos
    for _ in range(salidas):
        print("Introduza las coordenadas de los túneles (primero entrada, luego salida, separados por espacios): ")
        i1, j1, i2, j2 = map(int, input().rstrip().split())
        salidas_dict[(i1 - 1, j1 - 1)] = (i2 - 1, j2 - 1)
        salidas_dict[(i2 - 1, j2 - 1)] = (i1 - 1, j1 - 1)

    estados = [(-1, -1)]  # Estado de muerte.
    estado_a_indice = dict()
    valores = [0.0]  # Valores de los estados, es decir, probabilidades.
    estado_inicial = -1
    transiciones = [[(0, 1.0)]]  # Bucle propio cuando está muerto.

    # Asignación de índices a los estados del tablero
    for i1 in range(filas):
        for j1 in range(columnas):
            celda = tablero[i1][j1]
            
            if celda in ["A", "%", "O"]:
                estado_a_indice[(i1, j1)] = len(estados)
                estados.append((i1, j1))
            elif celda in ["#", "*"]:
                estado_a_indice[(i1, j1)] = 0       
            else:
                assert False, celda
    
    # Construcción de las transiciones entre estados
    for i1 in range(filas):
        for j1 in range(columnas):
            celda = tablero[i1][j1]
            indice_estado = estado_a_indice[(i1, j1)]

            if celda in ["A", "%", "O"]:
                if celda == "A":
                    estado_inicial = indice_estado
                    valores.append(0.0)
                elif celda == "%":
                    valores.append(1.0)
                    transiciones.append([(indice_estado, 1.0)])  # Bucle propio cuando se alcanza la salida.
                elif celda == "O":
                    valores.append(0.0)
                else:
                    assert False, celda

                if celda in ["A", "O"]:
                    i2, j2 = salidas_dict.get((i1, j1), (i1, j1))
                    sucesores = []
                    muertes = 0
                    for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        i3, j3 = i2 + a, j2 + b
                        if (0 <= i3 < filas) and (0 <= j3 < columnas):
                            simbolo = tablero[i3][j3]
                            if simbolo in ["A", "%", "O"]:
                                sucesores.append((i3, j3))
                            elif simbolo == "*":
                                muertes += 1
                    if len(sucesores) == 0:
                        transiciones.append([(0, 1.0)])
                    else:
                        transicion = [(estado_a_indice[s], 1 / (len(sucesores) + muertes)) for s in sucesores]
                        if muertes > 0:
                            transicion.append((0, muertes / (len(sucesores) + muertes)))
                        transiciones.append(transicion)

    # Algoritmo de iteración de valor
    while True:
        valores_antiguos = valores.copy()

        for estado in range(len(estados)):
            suma = 0.0
            for sucesor, probabilidad in transiciones[estado]:
                suma += valores[sucesor] * probabilidad
            valores[estado] = suma

        seguir_iterando = any(abs(valores[estado] - valores_antiguos[estado]) > 1e-10 for estado in range(len(estados)))

        if not seguir_iterando:
            break

    print(f"Esta es la probabilidad de que Alef escape del laberinto: {valores[estado_inicial]*100}%")
