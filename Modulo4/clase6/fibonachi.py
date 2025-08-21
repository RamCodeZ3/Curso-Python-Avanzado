def fibonacci(n):
    fib_series = [0, 1]

    while len(fib_series) < n:
        next_num = fib_series[-1] + fib_series[-2]
        fib_series.append(next_num)

    return fib_series


if __name__ == '__main__':
    n = int(
        input(
            "Ingrese nro de digitos de la serie fibonacci a calcular : "
        )
    )
    serie = fibonacci(n)
    print("SERIE FIBONACCI DE LOS ", n, " NUMEROS : ")
    for s in serie:
        print(s)
