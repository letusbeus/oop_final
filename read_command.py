from contacts import data


def read_phone_book():
    global data
    counter = 1
    for name, phone in sorted(data.items()):
        print(f'{counter}. {name}, {phone}')
        counter += 1
