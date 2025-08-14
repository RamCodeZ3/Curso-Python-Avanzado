import math


def trigonometry():
    options = input(
        "\n 1.Seno \n 2.Conseno \n 3.Tangente \nQue operacion quiere realizar:"
    )
    angulo = int(input('Introduce el valor del angulo: '))
    try:

        if options == '1':
            result = math.sin(angulo)
            print(result)

        elif options == '2':
            result = math.cos(angulo)
            print(result)

        elif options == '3':
            result = math.tan(angulo)
            print(result)
        else:
            print('No es una opcion')

    except Exception as e:
        print("No es un numero: {}".format(e))


if __name__ == '__main__':
    trigonometry()
