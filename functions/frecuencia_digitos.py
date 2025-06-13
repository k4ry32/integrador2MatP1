def contar_frecuencia_digitos(dni):
    '''
    Cuenta cuantas veces aparece cada digito (0-9) en un DNI.
    Retorna un diccionario con el digito como clave y su frecuencia como valor.
    '''
    frecuencia = {}

    for digito in str(dni):
        if digito in frecuencia:
            frecuencia[digito] += 1
        else:
            frecuencia[digito] = 1

    return frecuencia


def imprimir_frecuencia_dni(nombre, dni):

    #Muestra por pantalla la frecuencia de cada dígito en el DNI de una persona.
    
    print(f"\nFrecuencia de digitos en el DNI de {nombre} ({dni}):")
    frecuencia = contar_frecuencia_digitos(dni)
    for digito, cantidad in sorted(frecuencia.items()):
        print(f"Digito {digito}: {cantidad} vez/veces")
        
