# Funciones relacionadas con conjuntos

# Obtiene el conjunto de digitos unicos de un DNI
def obtenerConjuntoDNI(dni):
    return set(dni)

<<<<<<< Updated upstream
def operaciones_conjuntos(conjuntosDNI):
    if not conjuntosDNI:
        return set(), set(), set(), set()

    union = set.union(*conjuntosDNI) # UNION
    interseccion = set.intersection(*conjuntosDNI) # INTERSECCION
=======
# Funcion para operaciones con conjuntos (UNION, INTERSECCION, DIFERENCIA, DIFERENCIA SIMETRICA)
def operaciones_conjuntos(dnis):
    if not dnis:
        return set(), set(), set(), set()

    # UNION
    union = set.union(*dnis) 

    # INTERSECCION
    interseccion = set.intersection(*dnis) 
>>>>>>> Stashed changes
    
    # DIFERENCIA
    # Copia el valor del primer conjunto y resta desde el siguiente en la lista hasta el ultimo.
    diferencia = dnis[0].copy()
    for conjunto in dnis[1:]:
        diferencia -= conjunto

    # DIFERENCIA SIMETRICA
    diferencia_sim = dnis[0].copy()
    for conjunto in dnis[1:]:
        diferencia_sim = dnis[0].symmetric_difference(conjunto)

    return union, interseccion, diferencia, diferencia_sim