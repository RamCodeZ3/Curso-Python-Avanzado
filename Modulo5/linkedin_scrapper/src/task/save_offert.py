import csv
from pathlib import Path
from prefect import task
from decouple import config

FILE_PATH = Path(config('PYTHON_PATH') + 'files/offers.csv')


@task(name='GUARDAR OFERTAS LABORALES EN CSV')
def save_offert(list_offert):
    with open(FILE_PATH, 'w') as file:
        writer = csv.DictWriter(
            file, fieldnames=['Puesto', 'Ubicacion', 'Url']
        )
        writer.writerow(list_offert)
