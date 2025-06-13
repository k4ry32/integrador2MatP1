from model.Persona import Persona
from functions.conjuntos import obtenerConjuntoDNI

def nueva_Persona():
    nombre = input("Ingrese el nombre de la persona: ")
    dni = input("Ingrese el DNI de la persona: ")
    anio_nacimiento = int(input("Ingrese el año de nacimiento de la persona: "))
    persona = Persona(nombre, dni, anio_nacimiento)
    return persona


def ingresar_Personas():
    personas = []
    cantidad_personas = int(input("Ingrese la cantidad de personas que desea ingresar: "))

    for i in range(cantidad_personas):
        persona = nueva_Persona()
        personas.append(persona)

    return personas

def obtenerConjuntoDnis(personas):
    dnis = []
    for persona in personas:
        conjunto_dni = obtenerConjuntoDNI(persona.dni)
        dnis.append(conjunto_dni)
        print(f'Conjunto DNI para {persona.nombre}: {conjunto_dni}')

    return dnis