"""
    Presentacion del Trabajo Practico
    Contiene el menu principal a los ejercicios realizados por los integrates del grupo.
"""
def menu():
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('- - - - - - - -  TP Grupal de Integración II- - - - - - - -')
    print('- - - - - - - - - -   Grupo SlowPoke   - - - - - - - - - -')
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')

    # MENU
    # Se presentan los ejercicios disponibles, el usuario ingresa una opcion y se ejecuta el ejercicio correspondiente
    # El menu se repite hasta que el usuario ingrese la opcion 0
    opcion = ''

    while opcion != '0':
        print('Ejercicios disponibles (ingrese el numero del ejercicio):')
        print('')
        print('Operaciones con DNIs')
        print('1. Ingreso de los DNIs')
        print('2. Generación de los conjuntos de dígitos únicos')
        print('3. Cálculo y visualización de: unión, intersección, diferencias y diferencia simétrica.')
        print('4. Con qué frecuencia aparece dígito en cada DNI')
        print('5. Suma total de los dígitos de cada DNI')
        print('6. Ejercicio 4')
        print('Operaciones con años de nacimiento')
        print('7. Ingreso de los años de nacimiento')
        print('8. Cuántos nacieron en años pares e impares')
        print('9. Comprobar si alguno nació después del 2000')
        print('10. Comprobar si alguno nació en año bisiesto')
        print('11. Calcular el producto cartesiano entre el conjunto de años y el conjunto de edades actuales')
        print('0. Salir')

        opcion = input('Ingrese una opcion: ')

        match opcion:
            case '1':
                print('Ejercicio 1')
            case '2':
                print('Ejercicio 2')
            case '3':
                print('Ejercicio 3')
            case '4':
                print('Ejercicio 4')
            case '5':
                print('Ejercicio 5')
            case '6':
                print('Ejercicio 6')
            case '7':
                print('Ejercicio 7')
            case '8':
                print('Ejercicio 8')
            case '9':
                print('Ejercicio 9')
            case '10':
                print('Ejercicio 10')
            case '11':
                print('Ejercicio 11')
            case '0':
                print('Gracias por usar nuestro programa! Vuelve pronto!')
                break
            case _:
                print('No es una opcion valida. Intente nuevamente.')
                
        print('\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')


# EJECUCION DEL MENU PRINCIPAL
menu()# Punto de entrada, contiene la función principal y el menú interactivo