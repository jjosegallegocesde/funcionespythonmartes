'''numeroUno=5
numeroDos=10
sumatoria=numeroUno+numeroDos
print(f"La suma es {sumatoria}")'''

#DECLARANDO UNA FUNCIÓN

def sumar(numeroUno, numeroDos):
    sumatoria=numeroUno + numeroDos
    return sumatoria
    '''input("Ingrese el primer número: ")
    numUno = int(input())
    input("Ingrese el segundo número:  ")
    numDos = int(input())
    return numUno + numDos'''

#LLAMANDO UNA FUNCIÓN TRADICIONAL
numeroUno=int(input("ingrese el número 1: "))
numeroDos=int(input("ingrese el número 2: "))
numeroTres=int(input("ingrese el número 3: "))
resultado=sumar(numeroUno,numeroTres)
print(f"El resultado de la suma es {resultado}")

