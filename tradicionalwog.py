# numero_uno = 5
# numero_dos = 10
# sumatoria=numero_uno + numero_dos

# print(f"La suma es {sumatoria}")

# numero_tres = 5
# numero_cuatro = 10
# sumatoria_dos=numero_tres + numero_cuatro

# print(f"La suma es {sumatoria_dos}")

#declarando una funcion

def sumar_numeros (numero_uno, numero_dos):

    sumatoria=numero_uno+numero_dos

    return    sumatoria

#llamando una funcion tradicional

numero_uno=5
numero_dos=20
numero_tres=50

resultado= sumar_numeros (numero_uno,numero_tres)

print(f"la suma es: {resultado}")