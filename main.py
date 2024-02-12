import json

# Функция для вывода записей из справочника постранично на экран
def show_contacts(contacts, page_num, page_size):
    start = (page_num - 1) * page_size
    end = start + page_size
    page_contacts = contacts[start:end]
    for contact in page_contacts:
        print(f"Фамилия: {contact['фамилия']}")
        print(f"Имя: {contact['имя']}")
        print(f"Отчество: {contact['отчество']}")
        print(f"Организация: {contact['организация']}")
        print(f"Рабочий телефон: {contact['телефон рабочий']}")
        print(f"Личный телефон: {contact['телефон личный']}")
        print("---------------------------")

# Функция для добавления новой записи в справочник
def add_contact(contacts):
    contact = {}
    contact['фамилия'] = input("Введите фамилию: ")
    contact['имя'] = input("Введите имя: ")
    contact['отчество'] = input("Введите отчество: ")
    contact['организация'] = input("Введите название организации: ")
    contact['телефон рабочий'] = input("Введите рабочий телефон: ")
    contact['телефон личный'] = input("Введите личный телефон: ")
    contacts.append(contact)
    return contacts

# Функция для редактирования записи в справочнике
def edit_contact(contacts):
    index = int(input("Введите индекс записи, которую хотите отредактировать: "))
    if index < 0 or index >= len(contacts):
        print("Некорректный индекс")
        return contacts
    contact = contacts[index]
    contact['фамилия'] = input("Введите фамилию: ")
    contact['имя'] = input("Введите имя: ")
    contact['отчество'] = input("Введите отчество: ")
    contact['организация'] = input("Введите название организации: ")
    contact['телефон рабочий'] = input("Введите рабочий телефон: ")
    contact['телефон личный'] = input("Введите личный телефон: ")
    return contacts

# Функция для поиска записей по одной или нескольким характеристикам
def search_contacts(contacts):
    search_results = []
    surname = input("Введите фамилию для поиска: ")
    for contact in contacts:
        if contact['фамилия'].lower() == surname.lower():
            search_results.append(contact)
    return search_results

# Функция для сохранения справочника в текстовый файл
def save_contacts(contacts, file_path):
    with open(file_path, 'w') as file:
        json.dump(contacts, file)

# Функция для загрузки справочника из текстового файла
def load_contacts(file_path):
    try:
        with open(file_path, 'r') as file:
            contacts = json.load(file)
            return contacts
    except FileNotFoundError:
        return []

# Основная программа
file_path = 'contacts.txt'
contacts = load_contacts(file_path)
page_size = 5

while True:
    print("[1] Вывести записи постранично")
    print("[2] Добавить новую запись")
    print("[3] Редактировать запись")
    print("[4] Поиск записей")
    print("[0] Выход")
    choice = input("Введите номер операции: ")

    if choice == '1':
        page_num = int(input("Введите номер страницы: "))
        show_contacts(contacts, page_num, page_size)
    elif choice == '2':
        contacts = add_contact(contacts)
        save_contacts(contacts, file_path)
        print("Запись добавлена")
    elif choice == '3':
        contacts = edit_contact(contacts)
        save_contacts(contacts, file_path)
        print("Запись отредактирована")
    elif choice == '4':
        search_results = search_contacts(contacts)
        if len(search_results) > 0:
            show_contacts(search_results, 1, len(search_results))
        else:
            print("Записи не найдены")
    elif choice == '0':
        break
    else:
        print("Некорректный выбор")

print("Программа завершена")
