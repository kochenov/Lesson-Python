import time


def main_menu():
    print('************ Телефонный справочник ************\n')

    print('1 - Показать все контакты\n'
          '2 - Найти запись\n'
          '3 - Добавить новый контакт\n'
          '4 - Удалить контакт\n'
          '5 - Изменить данные контакта\n'
          '0 - Выход')


def writeFile(file_name):

    print('*** Добавление нового контакта ***\n')
    while True:
        with open(file_name, 'a', encoding='utf-8') as data:
            last_name = input('Фамилия: ')
            first_name = input('Имя: ')
            patronymic = input('Отчество: ')
            phone_number = input('Номер телефона: ')
            data.writelines(
                f'{last_name} {first_name} {patronymic} {phone_number}\n')
            choice = input(
                '\nНажмите Enter чтобы добавить новый контакт\nВведите 0 для выхода\n')
            if choice == '0':
                return


def readFile(file_name):

    print('*** Список контактов *** \n')

    with open(file_name, 'r', encoding='utf-8') as data:
        line = data.readlines()
    for i in line:
        i = line.index(i)
        print(f'{i + 1}. {line[i].strip()}')
    choice = input('\nНажмите Enter для выхода\n')
    if choice == ' ':
        return


def findContactByKeyWord(file_name):

    print('*** Поиск контакта *** \n')

    key_word = input(
        'Введите ФИО или номер телефона для поиска: ').casefold()
    with open(file_name, 'r', encoding='utf-8') as data:
        count = 0
        for line in data:
            if key_word in line.casefold():
                print(line)
                count += 1
        if count == 0:
            print('Контакт не найден.')
        else:
            print(f'Найдено контактов: {count}')
    choice = input('\nНажмите Enter для выхода\n')
    if choice == ' ':
        return


def DeleteContact(file_name):
    print('*** Удаление контакта *** \n')
    while True:
        with open(file_name, 'r', encoding='utf-8') as data:
            line = data.readlines()

        for i in line:
            i = line.index(i)
            print(f'{i + 1}. {line[i].strip()}')

        deleted_str = int(
            input('Введите порядковый номер контакта, который хотите удалить: '))
        del line[deleted_str - 1]

        with open(file_name, 'w', encoding='utf-8') as data:
            for i in line:
                data.write(i)
        choice = input(
            '\nНажмите Enter, чтобы продолжить удаление контактов\nВведите 0 для выхода\n')
        if choice == '0':
            return


def ReplaceData(file_name):
    print('*** Изменение данных ***\n')
    while True:
        with open(file_name, 'r', encoding='utf-8') as data:
            line = data.readlines()

        for i in line:
            i = line.index(i)
            print(f'{i + 1}. {line[i].strip()}')

        contact_id = int(input('Введите порядковый номер контакта: '))
        result = line[contact_id - 1].split()

        answer = int(input('Какие данные хотите изменить?\n'
                           '1 - Фамилия\n'
                           '2 - Имя\n'
                           '3 - Отчество\n'
                           '4 - Номер телефона\n'
                           '0 - для выхода\n'))

        if (answer == 1) or (answer == 2) or (answer == 3) or (answer == 4):
            rewrite_data(result, answer, line, contact_id, fileName)

        choice = input(
            '\nНажмите Enter, чтобы продолжить изменение контактов\nВведите 0 для выхода\n')
        if choice == '0':
            return


def rewrite_data(result, answer, line, contact_id, file_name):
    new_data = input("Введите новое значение: ")
    result[answer - 1] = new_data
    result[len(result) - 1] += '\n'
    line[contact_id - 1] = ' '.join(result)
    with open(file_name, 'w', encoding='utf-8') as data:
        for i in line:
            data.write(i)
