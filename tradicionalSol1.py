'''numeroUno=5
numeroDos=10
sumatoria =numeroUno+numeroDos
print (f"la suma es {sumatoria}")
numeroTres=5
numeroCuatro=10
sumatoria =numeroTres+numeroCuatro
print (f"la suma es {sumatoria}")'''

#Declarando una funcion tradicional
def sumarNumeros(numeroUno, numeroDos):
    sumatoria= numeroUno+numeroDos
    return sumatoria

#Llamando función tradicional
numeroUno=5
numeroDos=20
numeroTres=50
resultado= sumarNumeros(numeroUno,numeroTres)
print (f"la suma es:{resultado}")