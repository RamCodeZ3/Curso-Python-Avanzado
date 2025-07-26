"""
Programa para guardar datos de la pc
"""
import platform
import socket


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
        pc_file = open("pc.txt", 'w')
        pc_file.write(pc_data)
        pc_file.close()
        print('se consiguio los datos de manera exitosa')

    except Exception as e:
        print('No se encontro ningun archivo hubo un error: ' + e)


def read_file_pc():
    pc_file = open('pc.txt', 'r')
    pc_data = pc_file.read()
    pc_file.close
    print(pc_data)


if __name__ == '__main__':
    save_data_pc()
    read_file_pc()
