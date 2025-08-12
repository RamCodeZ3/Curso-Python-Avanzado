# Ejercicio de palindromo

def palindromo():
    Palabra = input("Introduce una palabra: ")
    if Palabra.replace(" ", "") == Palabra[::-1].replace(" ", ""):
        print(
            "Se lee de izquierda a derecha: Si es un palindromo"
        )

    else:
        print(
            "Esta palabra no es un palindromo: {} : {}".format(
                Palabra,
                Palabra[::-1]
            )
        )


if __name__ == "__main__":
    palindromo()
