
from csv import DictWriter, DictReader
from os.path import exists
import csv
# Дополнить справочник возможностью копирование данных из одного файла в другой.


def get_info():
    info = []
    first_name = input('Ввод фамилии: ')
    last_name = input('Ввод имени: ')
    info.append(first_name)
    info.append(last_name)
    flag = False
    while not flag:
        try:
            phone_number = int(input('Введите номер мобильный: '))
            if len(str(phone_number)) != 11:
                print('Номер набран не првильно')
            else:
                flag = True
        except ValueError:
            print('Такого номера не существут бро)')
    info.append(phone_number)
    return info


def create_file():
    with open('phone.csv', 'w', encoding='utf-8') as data:
        f_n_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_n_writer.writeheader()


def write_file(lst):
    with open('phone.csv', 'r', encoding='utf-8') as f_n:
        f_n_reader = DictReader(f_n)
        res = list(f_n_reader)
    with open('phone.csv', 'w', encoding='utf-8', newline='') as f_n:
        obj = {'Фамилия': lst[0], 'Имя': lst[1], 'Номер': lst[2]}
        res.append(obj)
        f_n_writer = DictWriter(f_n, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_n_writer.writeheader()
        for el in res:
            f_n_writer.writerow(el)


def read_file(file_name):
    with open(file_name, encoding='utf-8') as f_n:
        f_n_reader = DictReader(f_n)
        phone_book = list(f_n_reader)
    return phone_book



def search_user_index(file_name):
    info = input('Введите Фамилию или Имя: ').lower()
    row_num = None
    with open(file_name, 'r', encoding='utf-8') as data:
        data_reader = csv.reader(data)
        res = list(data_reader)
        for row in res:
            for el in row:
                if el.lower() == info:
                    row_num = int(res.index(row))
                    
    return row_num

def delete_file(file_name):
    with open(file_name, encoding='utf-8') as d:
        del_1 = list(DictReader(d))
        a = search_user_index('phone.csv')
        print_sep()
        del del_1[a - 1]
    with open('phone.csv', 'w', encoding='utf-8', newline='') as f_n:
        f_n_writer = DictWriter(f_n, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_n_writer.writeheader()
        for el in del_1:
            f_n_writer.writerow(el)


def write_file_ch(lst, a):
    with open('phone.csv', 'r', encoding='utf-8') as f_n:
        f_n_reader = DictReader(f_n)
        res = list(f_n_reader)
    with open('phone.csv', 'w', encoding='utf-8', newline='') as f_n:
        obj = {'Фамилия': lst[0], 'Имя': lst[1], 'Номер': lst[2]}
        res.insert(a - 1, obj)
        f_n_writer = DictWriter(f_n, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_n_writer.writeheader()
        for el in res:
            f_n_writer.writerow(el)

def change_file(file_name):
    a = search_user_index('phone.csv')
    info = input('Введите Фамилию или Имя: ').lower()
    print_sep()
    is_row = None
    with open(file_name, 'r', encoding='utf-8') as data:
        data_reader = csv.reader(data)
        res = list(data_reader)
        for row in res:
            for el in row:
                if el.lower() == info:
                    is_row = row

        if is_row != None:
            print('Есть совпадение !')
            print_sep()
            print(is_row)
            command = input('Изменить (1 - Фамилия | 2 - Имя | 3 - Номер): ')

            if command == '1':
                is_row[0] = input('Введи новое значение: ')
                print_sep()
            if command == '2':
                is_row[1] = input('Введи новое значение: ')
                print_sep()
            if command == '3':
                is_row[2] = input('Введи новое значение: ')
                print_sep()
            print(is_row)
        else:
            print('Совпадений не найдено !')
    print('Удалить старые данные !')
    print('Новые данные записаны !')
    write_file_ch(is_row, a)

def print_sep():
    print('============')


def record_info():
    lst = get_info()
    write_file(lst)


def main():
    while True:
        command = input("Введите команду: q-стоп; d-удаление; n- добавление; r-вывод данных; w-копирование данных")
        
        if command == 'q':
            break
        elif command == 'd':
            delete_file('phone.csv')
        elif command == 'n':
            change_file('phone.csv')
        elif command == 'r':
            if not exists('phone.csv'):
                print('Не удалосб создать файл')
                break
            print(*read_file('phone.csv'))
        elif command == 'w':
            if not exists('phone.csv'):
                create_file()
                record_info()
            else:
                record_info()


main()