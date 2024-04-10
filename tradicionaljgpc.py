'''
num1 = 5
num2 = 10
suma = num1 + num2
print(f"La suma es {suma}")

num3 = 5
num4 = 10
suma2 = num3 + num4
print(f"La suma es {suma2}")
'''

#Declarando una función
def sumar(num1, num2):
    suma = num1 + num2
    return suma

#Llamando una función tradicional
num1 = 5
num2 = 20
num3 = 50

resultado = sumar(num1, num3)
print(f"La suma es: {resultado}")