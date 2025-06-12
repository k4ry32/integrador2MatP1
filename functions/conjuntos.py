# Funciones relacionadas con conjuntos

# Obtiene el conjunto de digitos unicos de un DNI
def obtenerConjuntoDNI(dni):
    return set(dni)

#Suma recursivamente los digitos de un dni y devuelve la sumatoria de los mismos
def suma_digitos_DNI(numero):
        return numero if numero < 10 else (numero%10) + suma_digitos_DNI(numero//10)

#Expresion logica 1. Busca elementos en comun entre los conjuntos, al menos 4 de 5 grupos
def elementos_en_comun(conjunto1, conjunto2, conjunto3, conjunto4, conjunto5):
    #conjunto original
    conjuntos = [conjunto1, conjunto2, conjunto3, conjunto4, conjunto5]

    #une eliminado los duplicados
    todos_los_elementos = set().union(conjunto1,conjunto2,conjunto3,conjunto4,conjunto5)

    elementos_comunes = []
    #Buscamos cuales de ellos al menos estan 4 veces
    for elemento in todos_los_elementos:
        contador = 0
        for conjunto in conjuntos:
            if elemento in conjunto:
                contador += 1
        if contador >= 4:
            elementos_comunes.append(elemento)

    print("Elementos que están en al menos 4 de los 5 conjuntos:", elementos_comunes)


#Expresion logica 2. Evalua si entre todos los conjuntos, la sumatoria de los digitos pares som mas representativos que los impares
def grupoPar(conjunto1,conjunto2,conjunto3,conjunto4,conjunto5):
        conteo=0;
        arreglo=[conjunto1,conjunto2,conjunto3,conjunto4,conjunto5]
        for conjunto in arreglo:
                if sum(conjunto)%2==0:
                        conteo+=1
        if conteo>=3:
                print("El grupo es par")
        else:
                print("El grupo es impar")


#Expresion logica 3. 
#Indlica si es un numero primo o no
def es_primo(numero):
        estado=False
        #1 no es un numero primo
        if numero>1:
                contador=0
                for i in range(1,numero+1,1):
                        if numero%i ==0:
                                contador+=1
                if contador==2:
                        estado=True
                return estado

#Compara conjuntos si los iguales son primos
def sumatoria_igual_y_primos(conjunto1,conjunto2,conjunto3,conjunto4,conjunto5):
        arreglo=[conjunto1,conjunto2,conjunto3,conjunto4,conjunto5]
        for x in range(len(arreglo)):
                suma1=sum(arreglo[x])

                for y in range(x+1,len(arreglo)):
                        suma2=sum(arreglo[y])

                        if suma1==suma2:
                                if es_primo(suma1):
                                        print(f"Los conjuntos {x} e {y} son iguales ({suma1}) y son primos")