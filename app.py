
def suma(n1, n2):
    # Se verifica si son enteros
    if isinstance (n1,int) and isinstance(n2,int):
        return n1+n2
    # De otro modo siempre se obtendra 0
    return 0

print("PREGUNTA 1")
print("suma",suma(5,4))

def mas_ocurrencias(lista):
    # Inicialmente se utilizara 2 variables, ocurrencias(c) y numero(num)
    c = 0
    num = 0
    
    for i in lista:
        # La función COUNT(INDEX) nos sirve para encontrar rapidamente 
        # las ocurrencias de un elemento en una lista
        actual = lista.count(i)

        # Se compara si las ocurrencias del número actual 
        # superan al número de ocurrencias indicado incialemnte()
        if(actual > c):

            # Se actualiza el valor de las ocurrencias(c) con el valor que lo ha superado
            c = actual
            # Y por ultimo se captura el elemento
            num = i
    
    print("Cantidad",c)
    print("Número",num)
print("---------")
print("PREGUNTA 2")
mas_ocurrencias([1, 2, 2, 3, 4, 5, 8, 8, 8, 8, 7])

# Se utiliza una función para revertir el orden de la lista
def revertir(lista):
    lista = lista[::-1]
    return lista


def es_simetrica(lista):
    print(lista)
    # Se compara si la lista original es igual a la lista ya invertida    
    if lista == revertir(lista):
        return True
    # De otro modo siempre retornara falso
    return False
print("---------")      
print("PREGUNTA 3")
print(es_simetrica(['a','b','c','c','b','a']))
print(es_simetrica(['a','b','c','d']))


def multiplos_3_o_5(num):
    i = 1
    lista = []
    while (i < num):
        # Encontraremos los multiplos de 3 y 5,
        #  verificando si el resto de los números obtenidos es igual a 0
        if i%3 == 0 or i%5 == 0:
            # Si cumple con la condición se agregara a una lista
            lista.append(i) 
        i+=1
    #Con la lista ya actualizada, utilizamos la función SUM(LIST) 
    # para retornar la suma de todos los elemtnso de la lista
    return sum(lista)
print("---------")
print("PREGUNTA 4")
print("La suma es: ",multiplos_3_o_5(1000))

import math

#Definiremos el area para las respectivas figuras(cuadrado, círculo,triángulo,rectángulo)
def area_cuadrado(lado):
    return lado*lado

def area_circulo(radio):
    return radio*radio*math.pi

def area_triangulo(base,altura):
    return base*altura/2

def area_rectangulo(base,altura):
    return base*altura


print("---------")
print("PREGUNTA 5")
print("Cuadrado",area_cuadrado(1))
print("Cuadrado",area_cuadrado(2))
print("Cuadrado",area_cuadrado(3))

print("     ")

print("Circulo",area_circulo(4))
print("Circulo",area_circulo(5))
print("Circulo",area_circulo(6))

print("     ")

print("Triangulo",area_triangulo(7,8))
print("Triangulo",area_triangulo(8,9))
print("Triangulo",area_triangulo(9,10))

print("     ")

print("Rectangulo",area_rectangulo(10,11))
print("Rectangulo",area_rectangulo(11,12))
print("Rectangulo",area_rectangulo(12,13))

