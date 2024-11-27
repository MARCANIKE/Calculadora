def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Error: División por cero"
    return x / y

def calculadora():
    print("Seleccione la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    while True:
        eleccion = input("Ingrese el número de la operación (1/2/3/4): ")

        if eleccion in ['1', '2', '3', '4']:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            if eleccion == '1':
                print(f"{num1} + {num2} = {sumar(num1, num2)}")
            elif eleccion == '2':
                print(f"{num1} - {num2} = {restar(num1, num2)}")
            elif eleccion == '3':
                print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
            elif eleccion == '4':
                print(f"{num1} / {num2} = {dividir(num1, num2)}")

            siguiente_calculo = input("¿Quieres hacer otro cálculo? (sí/no): ")
            if siguiente_calculo.lower() != 'sí':
                break
        else:
            print("Opción no válida. Por favor, elija una operación válida.")

if __name__ == "__main__":
    calculadora()