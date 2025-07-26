# trabajo con archivos csv
import csv
from pathlib import Path

FILE_PATH = Path('users.csv')


def read_file_csv():
    try:
        with open(FILE_PATH, 'r') as file_csv:
            reader = csv.DictReader(file_csv)
            for row in reader:
                print(row)

    except FileNotFoundError as e:
        print(f"No se encontró el archivo: {e}")


def write_file_csv():
    try:
        with open(FILE_PATH, 'a') as file_csv:
            writer = csv.DictWriter(
                file_csv, fieldnames=['first_name', 'last_name', 'email']
            )

            writer.writerows([
                {
                    'first_name': 'Aram',
                    'last_name': 'Musset',
                    'email': 'arammussetam2@gmail.com'
                }
            ])

    except FileNotFoundError as e:
        print(f"No se encontró el archivo: {e}")


if __name__ == '__main__':
    read_file_csv()
    write_file_csv()
