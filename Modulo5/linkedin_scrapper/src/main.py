from prefect import flow
import logging
from task.get_offert import (
    get_offers
)
from task.save_offert import save_offert

log = logging.getLogger()

SKILL = 'python'


@flow(name='LINKEDIN SCRAPPER')
def main_flow():
    log.info("PROCESO DE EXTRACCIÓN")
    offers = get_offers(SKILL)
    save_offert(offers)
    print('¡Informacion guardada con exito!')


if __name__ == '__main__':
    main_flow()
