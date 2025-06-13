def contar_años_pares_impares(lista_años):
    """
    Recibe una lista de años y cuenta cuántos son pares e impares.
    Retorna una tupla (pares, impares).
    """
    pares = 0
    impares = 0

    for año in lista_años:
        if año % 2 == 0:
            pares += 1
        else:
            impares += 1

    return pares, impares


def imprimir_resumen_par_impar(lista_años):
    """
    Imprime el resumen de cuantos años son pares e impares.
    """
    pares, impares = contar_años_pares_impares(lista_años)
    print(f"\nCantidad de personas nacidas en años pares: {pares}")
    print(f"Cantidad de personas nacidas en años impares: {impares}")

