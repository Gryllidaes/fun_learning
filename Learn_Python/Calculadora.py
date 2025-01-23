import tkinter as tk

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
    if b == 0:
        return "Error: División por cero"
    return a / b

# Creamos una función para realizar la operación seleccionada por el usuario
def realizar_operacion():
    # Obtenemos los valores ingresados por el usuario
    num1 = float(entry1.get())
    num2 = float(entry2.get())

    # Obtenemos la opción seleccionada por el usuario
    opcion = operacion_var.get()

    # Realizamos la operación seleccionada por el usuario
    if opcion == "Sumar":
        resultado = sumar(num1, num2)
    elif opcion == "Restar":
        resultado = restar(num1, num2)
    elif opcion == "Multiplicar":
        resultado = multiplicar(num1, num2)
    elif opcion == "Dividir":
        resultado = dividir(num1, num2)
    else:
        resultado = "Opción inválida"

    # Mostramos el resultado en la etiqueta de resultado
    result_label.config(text="El resultado es: " + str(resultado))

# Creamos la ventana principal
root = tk.Tk()
root.title("Calculadora")

# Creamos los widgets de la GUI
label1 = tk.Label(root, text="Ingrese el primer número:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Ingrese el segundo número:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

operacion_var = tk.StringVar(root)
operacion_var.set("Sumar")

operacion_menu = tk.OptionMenu(root, operacion_var, "Sumar", "Restar", "Multiplicar", "Dividir")
operacion_menu.pack()

boton = tk.Button(root, text="Realizar operación", command=realizar_operacion)
boton.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Iniciamos el bucle principal de la GUI
root.mainloop()