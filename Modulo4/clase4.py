import datetime
import re


def my_birthday():
    print(
        "Coloque su cumpleaño en el siguiente formato: Año/Mes/Dia"
    )
    birthday = input("")
    try:
        date = datetime.datetime.strptime(birthday, "%Y/%m/%d")
        result = date - datetime.datetime.today()

        date_format = r' days, \d{2}:\d{2}:\d{2}.\d{6}'
        result2 = re.sub(date_format, "", str(result))
        print('Faltan {} dias para tu cumpleaño :D'.format(result2))

    except Exception as e:
        print("El formato no es valido: ", e)


if __name__ == '__main__':
    my_birthday()
