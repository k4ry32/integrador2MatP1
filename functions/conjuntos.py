# Funciones relacionadas con conjuntos

# Obtiene el conjunto de digitos unicos de un DNI
def obtenerConjuntoDNI(dni):
    return set(dni)

def operaciones_conjuntos(conjuntosDNI):
    if not conjuntosDNI:
        return set(), set(), set(), set()

    union = set.union(*conjuntosDNI) # UNION
    interseccion = set.intersection(*conjuntosDNI) # INTERSECCION
    
    # DIFERENCIA
    # Copia el valor del primer conjunto y resta desde el siguiente en la lista hasta el ultimo.
    diferencia = conjuntosDNI[0].copy()
    for conjunto in conjuntosDNI[1:]:
        diferencia -= conjunto

    # DIFERENCIA SIMETRICA
    diferencia_sim = conjuntosDNI[0].copy()
    for conjunto in conjuntosDNI[1:]:
        diferencia_sim = conjuntosDNI[0].symmetric_difference(conjunto)

    return union, interseccion, diferencia, diferencia_sim
