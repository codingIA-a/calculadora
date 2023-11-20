#crear una calculadora interactiva que tome una entrada de usuario y realice 
#una de las cuatro operaciones básicas (suma, resta, multiplicación o división) 
#Tomando dos números que deberá pedir al usuario
#Para esto deberá crear al menos 4 funciones: una para cada operación matemática



#ejemplo función que muestra el menú
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
        opcion = int(input('Ingrese el número de la operación deseada: '))
        #resto del código

calculadora()
