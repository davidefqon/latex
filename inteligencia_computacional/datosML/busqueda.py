def resolver_puzzle_8(estado_inicial):
    estado_objetivo = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    limite = 0

    while True:
        resultado = busqueda_limitada_por_profundidad(estado_inicial, estado_objetivo, limite)
        if resultado is not None:
            return resultado
        limite += 1

def busqueda_limitada_por_profundidad(estado, objetivo, limite):
    print("----------------------------")
    print(limite)
    pila = [(estado, 0, None)]
    while pila:
        estado_actual, profundidad_actual, movimiento_previo = pila.pop()
        print("(",profundidad_actual," - ",movimiento_previo,")",estado_actual)
        if estado_actual == objetivo:
            return estado_actual
        if profundidad_actual == limite:
            continue
        movimientos_posibles = obtener_movimientos(estado_actual, movimiento_previo)
        for movimiento in movimientos_posibles:
            nuevo_estado = mover_celda(estado_actual, movimiento)
            if nuevo_estado:
                pila.append((nuevo_estado, profundidad_actual + 1, movimiento))
    return None

def obtener_movimientos(estado, movimiento_previo):
    index_cero = estado.index(0)
    n = int(len(estado) ** 0.5)
    movimientos = []
    dict_movimientos = {
        'arriba': index_cero - n if index_cero >= n else None,
        'abajo': index_cero + n if index_cero < n * (n - 1) else None,
        'izquierda': index_cero - 1 if index_cero % n != 0 else None,
        'derecha': index_cero + 1 if index_cero % n != (n - 1) else None,
    }
    inversos = {'arriba': 'abajo', 'abajo': 'arriba', 'izquierda': 'derecha', 'derecha': 'izquierda'}
    for mov, idx in dict_movimientos.items():
        if idx is not None and mov != inversos.get(movimiento_previo):
            movimientos.append(mov)
    return movimientos

def mover_celda(estado, movimiento):
    estado = estado[:]
    index_cero = estado.index(0)
    n = int(len(estado) ** 0.5)
    dict_movimientos = {
        'arriba': index_cero - n,
        'abajo': index_cero + n,
        'izquierda': index_cero - 1,
        'derecha': index_cero + 1,
    }
    if movimiento in dict_movimientos and dict_movimientos[movimiento] is not None:
        nuevo_index = dict_movimientos[movimiento]
        estado[index_cero], estado[nuevo_index] = estado[nuevo_index], estado[index_cero]
        return estado
    return None

estado_inicial = [0, 1, 2, 4, 5, 3, 7, 8, 6]
# estado_inicial = [1, 0, 2, 4, 5, 3, 7, 8, 6]
# estado_inicial = [1, 2, 0, 4, 5, 3, 7, 8, 6]
# estado_inicial = [1, 2, 3, 4, 5, 0, 7, 8, 6]
# estado_inicial = [1, 2, 3, 4, 5, 6, 7, 8, 0]
solucion = resolver_puzzle_8(estado_inicial)
print("Solucion encontrada:", solucion)