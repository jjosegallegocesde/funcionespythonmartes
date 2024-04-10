'''numeroUno=5
numeroDos=10
sumatoria=numeroUno+numeroDos
print(f"La suma es: {sumatoria}")

numeroTres=5
numeroCuatro=10
sumatoriaDos=numeroTres+numeroCuatro
print(f"La suma es: {sumatoriaDos}")'''
#Declarando una funcion
def sumarNumeros(numeroUno,numeroDos):
    sumatoria=numeroUno+numeroDos
    return sumatoria 

#Llamando una funcion tradicional
numeroUno=5
numeroDos=20
numeroTres=50 
resultado=sumarNumeros(numeroUno,numeroTres)
print(f"La suma es: {resultado}")