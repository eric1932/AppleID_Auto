import datetime
import logging


def info(*text):
    logging.info(text)
    print(datetime.datetime.now().strftime("%H:%M:%S"), "[INFO]", text)


def error(*text):
    logging.critical(text)
    print(datetime.datetime.now().strftime("%H:%M:%S"), "[ERROR]", text)
