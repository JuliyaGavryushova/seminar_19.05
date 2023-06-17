# Задача 8.1: Создать телефонный справочник с возможностью импорта и экспорта данных в формате .csv
# Информация о человеке:
# Фамилия, Имя, Телефон, Описание
# Корректность и уникальность данных не обязательны.
# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода.
# Выберите наиболее удобную структуру данных для хранения справочника.
# 2) CRUD: Create, Read, Update, Delete
# Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
# Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека.
# Берем первое совпадение по фамилии.
# Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
# Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv
# 4) импорт данных из текстового файла формата csv
# Используйте функции для реализации значимых действий в программе
# Усложнение.
# - Сделать тесты для функций
# - Разделить на model-view-controller

# user = ["surname", "name", "phone", "description"]
# phone_dic = {1: ["surname", "name", "phone", "description"], 2: ["surname", "name", "phone", "description"]}

from os.path import join, abspath, dirname

def data_entry() -> list:
    user = []
    user.append(input("Введите фамилию: "))
    user.append(input("Введите имя: "))
    user.append(input("Введите номер телефона: "))
    user.append(input("Введите комментарий: "))
    return user

# key_count = 0
# phone_dic = dict()

def creating_record(phone_dic_local: dict, idc: int, user: list) -> dict:
    idc += 1
    phone_dic_local[idc] = user
    return phone_dic_local, idc

# user1 = ["surname1", "name1", "phone1", "description1"]
# user2 = ["surname2", "name2", "phone2", "description2"]
# phone_dic, key_count = creating_record(phone_dic, key_count, user1)
# phone_dic, key_count = creating_record(phone_dic, key_count, user2)
# print(phone_dic)

def menu():
    print("Введите 0, если хотите выйти")
    print("Введите 1, если хотите внести пользователя")
    print("Введите 2, если хотите распечатать справочник")
    print("Введите 3, если хотите экспортировать")
    print("Введите 4 для поиска")
    print("Введите 5, если хотите удалить запись")
    print("Введите 6, если хотите изменить существующую запись")
    print("Введите 7 для импорта справочника")
    key_count = 0
    phone_dic = dict()
    while True:
        num = int(input("Введите номер операции: "))
        if num == 0:
            break
        if num == 1:
            user = data_entry()
            phone_dic, key_count = creating_record(phone_dic, key_count, user)
        if num == 2:
            print(phone_dic)
        if num == 3:
            file_name = input("Введите имя файла: ")
            export_phone_dic(phone_dic, file_name)
        if num == 4:
            search = input("Кого хотите найти: ")
            print(search_user(phone_dic, search))
        if num == 5:
            del_cont = input("Введите первые буквы контакта, который хотите удалить: ")
            deleting_contact(phone_dic, del_cont)
        if num == 6:
            update_cont = input("Введите первые буквы контакта, который хотите изменить: ")
            update_contact(phone_dic, update_cont)
        if num == 7:
            file_name = input("Введите имя файла: ")
            import_phone_dic(phone_dic, file_name)

def export_phone_dic(phone_dic: dict, file_name: str):
    MAIN_DIR = abspath(dirname(__file__))
    full_name = join(MAIN_DIR, file_name + ".txt")
    with open(full_name, mode="w", encoding="utf-8") as file:
        for idc, user in phone_dic.items():
            file.write(f"{idc},{user[0]},{user[1]},{user[2]},{user[3]}\n")

def search_user(phone_dic: dict, search: str) -> int:
    for idc, user in phone_dic.items():
        if user[0].startswith(search):
            return idc, user
        
def deleting_contact(phone_dic: dict, del_cont: str):
    tmp = search_user(phone_dic, del_cont)
    if tmp is not None:
        idc, _ = tmp
        phone_dic.pop(idc)
    else: print("Контакт не найден")
    return phone_dic

def update_contact(phone_dic: dict, update_cont: str):
    tmp = search_user(phone_dic, update_cont)
    if tmp is None:
        print("Контакт не найден")
        return phone_dic
    idc, _ = tmp
    new_surname = input("Введите фамилию: ")
    new_name = input("Введите имя: ")
    new_phone = input("Введите номер тел: ")
    new_description = input("Введите описание: ")
    if len(new_surname) >= 1:
        phone_dic[idc][0] = new_surname
    if len(new_name) >= 1:
        phone_dic[idc][1] = new_name
    if len(new_phone) >= 1:
        phone_dic[idc][2] = new_phone
    if len(new_description) >= 1:
        phone_dic[idc][3] = new_description
    return phone_dic
    
def import_phone_dic(phone_dic: dict, file_name: str):
    MAIN_DIR = abspath(dirname(__file__))
    full_name = join(MAIN_DIR, file_name + ".txt")
    idc = 0
    phone_dic = dict()
    with open(full_name, mode="r", encoding="utf-8") as file:
        for line in file:
            lst = line.strip().split('#')[1:]
            phone_dic, idc = creating_record(phone_dic, idc, lst)
    return phone_dic, idc
        



# phone_dir = {1: ['Иванов',   'Иван',  '+7(xxx)xxx-xx-xx', 'desription_Иванов'], 
#             2: ['Петров',   'Петр',  '+7(---)xxx-xx-xx', 'desription_Петров'], 
#             3: ['Соколов',  'Илья',  '+7(---)---------', 'desription_Соколов'], 
#             4: ['Павельев', 'Андрей','+7(***)***-**-**', 'desription_Павельев'], 
#             5: ['Пешехов',  'Антон', '+7++++++++++',     'desription_Пешехов'], 
#             6: ['Сааков',   'Илья',  '+7(+++)+++-++-++', 'desription_Сааков'], 
#             }
# print(search_user(phone_dir, "Пеш"))


menu()
# export_phone_dic(phone_dic, "telephone_directory")