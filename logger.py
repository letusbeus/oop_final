from datetime import datetime


def add_logger(data):
    time = datetime.now().strftime('%H:%M')
    with open("log.csv", "a") as file:
        file.write(f'{time} added {data}.\n')


def del_logger(data):
    time = datetime.now().strftime('%H:%M')
    with open("log.csv", "a") as file:
        file.write(f'{time} deleted {data}.\n')


def edit_logger(data):
    time = datetime.now().strftime('%H:%M')
    with open("log.csv", "a") as file:
        file.write(f'{time} edited {data}.\n')


def error_logger(error):
    time = datetime.now().strftime('%H:%M')
    with open("error.csv", "a") as file:
        file.write(f'{time} error message: {error}.\n')
