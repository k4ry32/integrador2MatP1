from functions import conjuntos
from utils import mock

personas = mock.crearPersonas()
#for persona in personas:
#    print(persona)

conjuntosDNI = []

for persona in personas:
    conjDNI = conjuntos.obtenerConjuntoDNI(persona.dni)
    conjuntosDNI.append(conjDNI)

print(conjuntos.operaciones_conjuntos(conjuntosDNI))
