"""
Programa para guardar datos de la pc
"""
import platform
import socket
from pathlib import Path

FILE_PATH = Path('pc.txt')


def save_data_pc():
    try:
        pc_data = "=========== Informacion de la pc ===========  \n"
        pc_data += f"""
    sistema operativo: {platform.system()}, {platform.version()}\n
    Arquitectura: {platform.machine()}\n
    Procesador: {platform.processor()}\n
    Hostname: {socket.gethostname()}\n
    Ip: {socket.gethostbyname(socket.gethostname())}
    """
        with open(FILE_PATH, 'w') as pc_file:
            pc_file.write(pc_data)

        print('se consiguio los datos de manera exitosa')

    except Exception as e:
        print('No se encontro ningun archivo hubo un error: ' + e)


def read_file_pc():
    try:
        with open(FILE_PATH, 'r') as pc_file:
            pc_data = pc_file.read()
            print(pc_data)

    except Exception as e:
        print('No se pudo leer el archivo hubo un error: ' + e)


if __name__ == '__main__':
    save_data_pc()
    read_file_pc()
