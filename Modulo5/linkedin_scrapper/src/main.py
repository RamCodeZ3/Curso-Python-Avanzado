from prefect import flow
import logging

log = logging.getLogger()

SKILL = 'python'


@flow(name='LINKEDIN SCRAPPER')
def main_flow():
    log.info("PROCESO DE EXTRACCIÓN")


if __name__ == '__main__':
    main_flow()
