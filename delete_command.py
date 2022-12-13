from contacts import data
import logger as log


def delete_contact(user_data):
    global data
    for name, phone in data.copy().items():
        if phone == user_data:
            del data[name]
            log.del_logger(f'{name} {phone}')
