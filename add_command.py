from contacts import data
import logger as log


def add_contact(name, surname, phonenumber):
    global data
    data[f'{name} {surname}'] = phonenumber
    log.add_logger(f'{name} {surname} {phonenumber}')
    return data


def add_bot(name, surname, phonenumber):
    global data
    data[f'{name} {surname}'] = phonenumber
    log.add_logger(f'{name} {surname} {phonenumber}')