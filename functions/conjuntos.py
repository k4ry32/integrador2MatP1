# Funciones relacionadas con conjuntos

# Obtiene el conjunto de digitos unicos de un DNI
def obtenerConjuntoDNI(dni):
    return sorted(set(dni))

# Funcion para operaciones con conjuntos (UNION, INTERSECCION, DIFERENCIA, DIFERENCIA SIMETRICA)
def operaciones_conjuntos(dnis):
    if not dnis:
        return set(), set(), set(), set()

    # UNION
    union = set.union(*dnis) 

    # INTERSECCION
    interseccion = set.intersection(*dnis) 
    
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


# Funcion para obtener el producto cartesiano entre los conjuntos de años y edades
def obtenerProductoCartesiano(conjunto1, conjunto2):
    nuevoConjunto = []

    # Se recorre el conjunto 1, por cada elemento se lo une con los elementos del conjunto 2
    for x in conjunto1:
        for y in conjunto2:
            newTuple = (x, y)
            nuevoConjunto.append(newTuple)

    return nuevoConjunto