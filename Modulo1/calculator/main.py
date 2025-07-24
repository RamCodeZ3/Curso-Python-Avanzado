def add(a, b): return a+b


def subtract(a, b):
    return a-b


def multiply(a, b):
    return a*b


def divide(a, b):
    if b != 0:
        return a/b
    else:
        return 'Error'


def main():
    print("Calculadora básica")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    choice = input("Elige una opción (1-4): ")
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))

    if choice == '1':
        print("Resultado:", add(a, b))

    elif choice == '2':
        print("Resultado:", subtract(a, b))

    elif choice == '3':
        print("Resultado:", multiply(a, b))

    elif choice == '4':
        print("Resultado:", divide(a, b))

    else:
        print("Opción inválida")


main()
