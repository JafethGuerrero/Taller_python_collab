def imprimir_nombre_completo(nombre, apellido, carrera):
    print(f'Mi nombre es {nombre} {apellido} y pertenezco a la carrera de {carrera}')


def calculadora_basica(x, y, operacion):
    """
    operacion:
        1 -> suma
        2 -> resta
        3 -> multiplicación
        4 -> división
    """
    if operacion == 1:
        return x + y
    elif operacion == 2:
        return x - y
    elif operacion == 3:
        return x * y
    elif operacion == 4:
        return x / y
    else:
        raise ValueError("Operación no válida")


def promedio_lista(lista):
    return sum(lista) / len(lista)


def contar_pares_y_convertir(lista):
    """
    Recibe una lista de enteros.
    Regresa:
      - cantidad de pares
      - lista con los impares convertidos a pares (+1)
    """
    cantidad_pares = sum(1 for n in lista if n % 2 == 0)
    lista_convertida = [n if n % 2 == 0 else n + 1 for n in lista]
    return cantidad_pares, lista_convertida
