# ввод данных от пользователя
import validate
import time


def main_menu():
    print('Главное меню телефонного справочника')
    mode = input('1. записать в книгу\n2. показать кигу\n3. найти данные'
                 '\n4. выход\n введите 1, 2, 3  или 4: ')
    if mode in '1234':
        return int(mode)
    else:
        print('проверь ввод')


def write_data():
    phone_record = [input('введите фамилию: ').title(), input('введите имя: ').title()]
    phone = ''
    while not validate.check_phone(phone):
        phone = input('введите номер телефона: ')
        if not validate.check_phone(phone):
            print('повтори ввод телефона')
    phone_record.append(phone)
    description = input('Введите описание: ')
    if description:
        phone_record.append(description)
    print(f'Запись внесена в книгу: {str.join(", ", phone_record)}')
    return phone_record


def search_data():
    return input('ведите фамилию или номер: ').title()


def show_data(data):
    print(f'Найдено записей: {len(data)}')
    for line in data:
        print(line)

def show_ext_data(data):
    print(f'Найдено записей: {len(data)}\n')
    for line in data:
        for text in line:
            print(text)
