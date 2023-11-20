#crear una calculadora interactiva que tome una entrada de usuario y realice 
#una de las cuatro operaciones básicas (suma, resta, multiplicación o división) 
#Tomando dos números que deberá pedir al usuario dentro de la función calculadora()
#Para esto deberá crear al menos 4 funciones: una para cada operación matemática
#Las cuatro funciones deben ser creadas por separado, pero, una vez creadas, deberá integrar cada una de ellas dentro
#de la función calculadora()

import time

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "No es posible dividir por cero."

def mostrar_menu():
    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

def calculadora():
    while True:
        mostrar_menu()
        opcion = int(input("Ingrese el número de la operación deseada: "))

        if opcion > 0 and opcion <=5:
            if opcion == 5:
                print("¡Hasta luego!")
                break

            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
            except ValueError:
                print("Error: Ingrese números válidos.")
                continue

            if opcion == 1:
                resultado = suma(num1, num2)
            elif opcion == 2:
                resultado = resta(num1, num2)
            elif opcion == 3:
                resultado = multiplicacion(num1, num2)
            elif opcion == 4:
                resultado = division(num1, num2)
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
                continue
            
            print("El resultado es:", resultado)
            time.sleep(2)
            print('\n')
        else:
            print('\n')
            print('Opción no válida!')
            print('Inténtalo Nuevamente')
            print('\n')
            time.sleep(1)
            
            

calculadora()
