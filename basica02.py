def main():
    numeros = []

    while True:
        print("\nMenu:")
        print("1. Ingresar 3 números")
        print("2. Sumar los números")
        print("3. Mostrar los números")
        print("4. Calcular el promedio")
        print("5. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            numeros = ingresar_numeros()
        elif opcion == "2":
            sumar_numeros(numeros)
        elif opcion == "3":
            mostrar_numeros(numeros)
        elif opcion == "4":
            calcular_promedio(numeros)
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 5.")

def ingresar_numeros():
    numeros = []
    for i in range(3):
        numero = int(input(f"Ingrese el número {i + 1}: "))
        numeros.append(numero)
    print("Números ingresados correctamente.")
    return numeros

def sumar_numeros(numeros):
    if len(numeros) == 3:
        suma = sum(numeros)
        print(f"La suma de los números es: {suma}")
    else:
        print("Debe ingresar 3 números antes de sumarlos.")

def mostrar_numeros(numeros):
    if len(numeros) == 3:
        print(f"Los números ingresados son: {numeros}")
    else:
        print("Debe ingresar 3 números antes de mostrarlos.")

def calcular_promedio(numeros):
    if len(numeros) == 3:
        promedio = sum(numeros) / len(numeros)
        print(f"El promedio de los números es: {promedio}")
    else:
        print("Debe ingresar 3 números antes de calcular el promedio.")

if __name__ == "__main__":
    main()
