from utils.mock import crearPersonas
from functions.operaciones import *
from functions.conjuntos import *
from functions.frecuencia_digitos import imprimir_frecuencia_dni
from functions.años_par_impar import imprimir_resumen_par_impar
from functions.definir_persona import ingresar_Personas, obtenerConjuntoDnis

"""
    Presentacion del Trabajo Practico
    Contiene el menu principal a los ejercicios realizados por los integrates del grupo.
"""

def menu():
    personas = None
    dnis = None

    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('- - - - - - - -  TP Grupal de Integración II- - - - - - - -')
    print('- - - - - - - - - -   Grupo SlowPoke   - - - - - - - - - -')
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')

    # MENU
    # Se presentan los ejercicios disponibles, el usuario ingresa una opcion y se ejecuta el ejercicio correspondiente
    # El menu se repite hasta que el usuario ingrese la opcion 0
    opcion = ''

    while opcion != '0':
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')
        print('Ejercicios disponibles (ingrese el numero del ejercicio):')
        print('')
        print('Operaciones con DNIs')
        print('1. Ingreso de datos de integrantes del grupo')
        print('2. Generación de los conjuntos de dígitos únicos')
        print('3. Cálculo y visualización de: unión, intersección, diferencias y diferencia simétrica.')
        print('4. Con qué frecuencia aparece cada dígito en cada DNI')
        print('5. Suma total de los dígitos de cada DNI')
        print('6. Evaluación de condiciones lógicas planteadas')
        print('Operaciones con años de nacimiento')
        print('7. Cuántos nacieron en años pares e impares')
        print('8. Comprobar si el grupo es de la Generacion Z (después de 2000)')
        print('9. Comprobar si alguno nació en año bisiesto')
        print('10. Calcular el producto cartesiano entre el conjunto de años y el conjunto de edades actuales')
        print('0. Salir')

        opcion = input('\nIngrese una opcion: ')
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')

        if int(opcion) > 1 and personas is None:
            print('Se crearon personas automaticamente.\n')
            personas = crearPersonas()
            
        if int(opcion) > 2 and dnis is None:
            dnis = obtenerConjuntoDnis(personas)

        match opcion:
            case '1':
                print('Desea ejecutar la función automática para ingresar los estudiantes o ingresarlos manualmente?')
                print('1. Ingresar estudiantes manualmente')
                print('2. Función automática')
                op = input('Ingrese una opcion: ')
                match op:
                    case '1':
                        personas = ingresar_Personas()
                    case '2':
                        personas = crearPersonas()

                if personas is not None:
                    for persona in personas:
                        print(persona)

            case '2':
                if personas is not None:
                    for persona in personas:
                        print(f'Conjunto DNI para {persona.nombre}: {obtenerConjuntoDNI(persona.dni)}')        
                    
            case '3':
                print(operaciones_conjuntos(dnis))
            case '4':
                if personas is not None:
                    for persona in personas:
                        imprimir_frecuencia_dni(persona.nombre, persona.dni)
            case '5':
                if personas is not None:
                    for persona in personas:
                        print(f'La suma de los dígitos de {persona.dni} es: {suma_digitos_DNI(int(persona.dni))}')
            case '6':
                if dnis is not None:
                    print('Condiciones lógicas:')
                    print('1. Existe al menos 1 elemento que pertenece a 4 de 5 conjuntos')
                    elementos_en_comun(dnis[0], dnis[1], dnis[2], dnis[3], dnis[4])

                    print('2. Si hay más conjuntos donde la suma de sus elementos es par, entonces se considera que es un "grupo par"')
                    grupoPar(dnis[0], dnis[1], dnis[2], dnis[3], dnis[4])

                    print('3. Existen 2 conjuntos donde la suma de sus elementos dan el mismo numero, que además es un numero primo')
                    sumatoria_igual_y_primos(dnis[0], dnis[1], dnis[2], dnis[3], dnis[4])
            case '7':
                if personas is not None:
                    anios = []
                    for persona in personas:
                        anios.append(persona.anio_nacimiento)

                    imprimir_resumen_par_impar(anios)
            case '8':
                generacionZ(personas)
            case '9':
                nacido_en_bisiesto(personas)
            case '10':
                conjuntoEdades = []
                conjuntoAnios = []

                if personas is not None:
                    for persona in personas:
                        conjuntoEdades.append(persona.edad)
                        conjuntoAnios.append(persona.anio_nacimiento)
                
                productoCartesiano = obtenerProductoCartesiano(sorted(conjuntoAnios), sorted(conjuntoEdades))

                print('Producto cartesiano:')                
                for row in productoCartesiano:
                    print(row)
            
            case '0':
                print('Gracias por usar nuestro programa! Vuelve pronto!')
                break
            case _:
                print('No es una opcion valida. Intente nuevamente.')
                
        print('\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')


# EJECUCION DEL MENU PRINCIPAL
menu()# Punto de entrada, contiene la función principal y el menú interactivo