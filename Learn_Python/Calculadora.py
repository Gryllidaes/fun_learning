# Definimos una función para sumar dos números
def sumar(a, b):
    return a + b

# Definimos una función para restar dos números
def restar(a, b):
    return a - b

# Definimos una función para multiplicar dos números
def multiplicar(a, b):
    return a * b

# Definimos una función para dividir dos números
def dividir(a, b):
    return a / b

# Pedimos al usuario que ingrese los dos números para realizar la operación
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Mostramos el menú de opciones de operaciones
print("Seleccione una operación:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

# Pedimos al usuario que seleccione una operación
opcion = int(input("Ingrese una opción (1/2/3/4): "))

# Realizamos la operación seleccionada por el usuario
if opcion == 1:
    print(num1, "+", num2, "=", sumar(num1, num2))
elif opcion == 2:
    print(num1, "-", num2, "=", restar(num1, num2))
elif opcion == 3:
    print(num1, "*", num2, "=", multiplicar(num1, num2))
elif opcion == 4:
    print(num1, "/", num2, "=", dividir(num1, num2))
else:
    print("Opción inválida")