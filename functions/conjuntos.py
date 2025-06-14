# Funciones relacionadas con conjuntos

# Obtiene el conjunto de digitos unicos de un DNI
def obtenerConjuntoDNI(dni):
    return set(dni)

# Funcion para operaciones con conjuntos (UNION, INTERSECCION, DIFERENCIA, DIFERENCIA SIMETRICA)
def operaciones_conjuntos(dnis, personas):
    if not dnis:
        return set(), set(), set(), set()

    # UNION
    union = set.union(*dnis) 

    # INTERSECCION
    interseccion = set.intersection(*dnis) 

    # DIFERENCIA SIMETRICA
    diferencia_sim = union - interseccion

    print("Operaciones con conjuntos:\n\n")
    for persona in personas:
        print(f"Nombre: {persona.nombre}, DNI: {persona.dni}, Conjunto DNI: {obtenerConjuntoDNI(persona.dni)}\n")
    print(f"\n\nUNION: {sorted(union)}\nINTERSECCION: {interseccion}\nDIF. SIMETRICA: {sorted(diferencia_sim)}\n")

    # DIFERENCIA
    i=-1
    for persona in personas:          
          print(f"DIFERENCIA entre {persona.nombre} y {personas[i].nombre}.\n{obtenerConjuntoDNI(persona.dni) - obtenerConjuntoDNI(personas[i].dni)}\n")
          i = i + 1

# Funcion para obtener el producto cartesiano entre los conjuntos de años y edades
def obtenerProductoCartesiano(conjunto1, conjunto2):
    nuevoConjunto = []

    # Se recorre el conjunto 1, por cada elemento se lo une con los elementos del conjunto 2
    for x in conjunto1:
        row = []
        for y in conjunto2:
            newTuple = (x, y)
            row.append(newTuple)
        nuevoConjunto.append(row)

    return nuevoConjunto