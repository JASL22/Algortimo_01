class Operaciones:
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b    

    def division(self, a, b):   
        if b == 0:
            return "Error: Division by zero"
        return a / b

def main():
    operaciones = Operaciones()
    valid_operations = {"suma", "resta", "multiplicacion", "division"}

    while True:
        try:
            a = int(input("Ingrese el primer número: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")

    while True:
        operacion = input("Ingrese la operación (suma, resta, multiplicacion, division): ").strip().lower()
        if operacion in valid_operations:
            break
        print("Operación no válida. Por favor, elija una operación válida.")

    while True:
        try:
            b = int(input("Ingrese el segundo número: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")

    if operacion == "suma":
        resultado = operaciones.suma(a, b)
    elif operacion == "resta":
        resultado = operaciones.resta(a, b)
    elif operacion == "multiplicacion":
        resultado = operaciones.multiplicacion(a, b)
    elif operacion == "division":
        resultado = operaciones.division(a, b)
    else:
        resultado = "Operación no válida"

    print("Resultado:", resultado)

if __name__ == "__main__":
    main()
