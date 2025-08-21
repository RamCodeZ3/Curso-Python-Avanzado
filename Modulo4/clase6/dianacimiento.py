import datetime


def dianacimiento(fecha):
    dias = [
        'lunes',
        'martes',
        'miercoles',
        'jueves',
        'viernes',
        'sabado',
        'domingo'
    ]
    dia_nacimiento = fecha.weekday()
    return dias(dia_nacimiento)


if __name__ == '__main__':
    fecha_string = input("Ingrese Fecha nacimiento (YYY-MM-DD) : ")
    fecha_objeto = datetime.datetime.strptime(fecha_string, "%Y-%m-%d")
    dia = dianacimiento(fecha_objeto)
    print(f"Naciste un {dia}")
