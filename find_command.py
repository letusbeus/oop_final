from contacts import data


def find_contact(user_data):
    global data
    filtered_list = []
    for name, phone in data.items():
        if (user_data.lower() in name.lower()) or (user_data in phone):
            filtered_list.append(f'{name}, {phone}')
    for idx, el in enumerate(filtered_list):
        print(idx + 1, el)
    return filtered_list
