import decimal


num1 = decimal.Decimal('12.9023')
num2 = decimal.Decimal('17.67')


def calculator_decimal(decimal1, decimal2):
    print(
        'La suma de estos decimales es igual a: {}'.format(
            decimal1+decimal2
            ))
    print(
        'La resta de estos decimales es igual a: {}'.format(
            decimal1-decimal2
            ))
    print(
        'La multiplicacion de estos decimales es igual a: {}'.format(
            decimal1*decimal2
            ))
    print(
        'La division de estos decimales es igual a: {}'.format(
            decimal1/decimal2))


def redondeo(num):
    print(
        'Este numero rendondeado es igual a: {}'.format(
            num.quantize(
                decimal.Decimal('0.00'))))


if __name__ == '__main__':
    calculator_decimal(num1, num2)
    redondeo(num1)
