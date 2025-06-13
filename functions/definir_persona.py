from model.Persona import Persona
from functions.conjuntos import obtenerConjuntoDNI

# Funcion para ingresar los datos de una persona
def nueva_Persona():
    nombre = input("Ingrese el nombre de la persona: ")
    dni = input("Ingrese el DNI de la persona: ")
    anio_nacimiento = int(input("Ingrese el año de nacimiento de la persona: "))
    persona = Persona(nombre, dni, anio_nacimiento)
    return persona

# Funcion para ingresar una cierta cantidad de personas (a eleccion del usuario)
def ingresar_Personas():
    personas = []
    cantidad_personas = int(input("Ingrese la cantidad de personas que desea ingresar: "))

    for i in range(cantidad_personas):
        persona = nueva_Persona()
        personas.append(persona)

    return personas

# Funcion para obtener el conjunto DNI de cada persona en una lista
def obtenerConjuntoDnis(personas):
    dnis = []
    for persona in personas:
        conjunto_dni = obtenerConjuntoDNI(persona.dni)
        dnis.append(conjunto_dni)

    return dnis