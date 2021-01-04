import sys

import requests
import logging as logger
logger.root.handlers = []
logger.basicConfig(level=logger.INFO, filename="Logs.log", filemode="a",
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def send_request(url, params):
    try:
        response = requests.get(url=url, params=params)
        return response
    except requests.ConnectionError as e:
        log(e, "error")
    except:
        log(sys.exc_info()[0], "error")


def extract_temperature_from_text(text):
    length = len(text)
    if length > 1:
        return text[:length-1]
    log("extracting temperature from text not successful for text = {}".format(text), level="info")


def is_valid_number(text):
    try:
        float(text)
        return True
    except ValueError as e:
        log(e,"error")
        return False
    except:
        log(sys.exc_info()[0],"error")


def log(message,level="info"):
    if level == "info":
        logger.info(message)
    elif level == "error":
        logger.error(message)
    elif level == "critical":
        logger.critical(message)