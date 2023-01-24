import methods

data_phone_db = './dataPhone.txt'

while True:
    methods.main_menu()
    item_menu = int(input('Выберете пункт меню: '))
    match item_menu:
        case 1:
            methods.readFile(data_phone_db)
        case 2:
            methods.findContactByKeyWord(data_phone_db)
        case 3:
            methods.writeFile(data_phone_db)
        case 4:
            methods.DeleteContact(data_phone_db)
        case 5:
            methods.ReplaceData(data_phone_db)
        case 0:
            print('Выхожу...')
            exit(0)
        case _:
            print('Такого пункта нет в меню...')
