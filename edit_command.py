import logger as log
from contacts import data


def change_contact_number(old_data, new_data):
    global data
    data[old_data] = new_data
    print(f'Номер абонента {old_data} изменен. Новый номер: {new_data}')
    log.edit_logger(f'{old_data} changed number to {new_data}')
    return data


def change_contact_name(old_data, new_data):
    global data
    data[new_data] = data.pop(old_data)
    print(f'Имя абонента {old_data} изменено. Новое имя: {new_data}')
    log.edit_logger(f'{old_data} changed name to {new_data}')
    return data


def bot_change_contact_number(old_data, new_data):
    global data
    data[old_data] = new_data
    log.edit_logger(f'{old_data} changed number to {new_data}')
    return data


def bot_change_contact_name(old_data, new_data):
    global data
    data[new_data] = data.pop(old_data)
    log.edit_logger(f'{old_data} changed name to {new_data}')
    return data
