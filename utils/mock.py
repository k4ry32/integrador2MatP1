from model.Persona import Persona

# Mock de grupo para agilizar pruebas
def crearPersonas():
    personas = []
    
    personas.append(Persona("Gaston", "43060097", 2005))
    personas.append(Persona("Javier", "32793185", 1988))
    personas.append(Persona("Celeste", "45028610", 2007))
    personas.append(Persona("Bruno", "31702911", 1987))
    personas.append(Persona("Karina", "36168847", 1991))

    return personas