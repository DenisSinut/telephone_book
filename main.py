import csv
from prettytable import PrettyTable


def load_book():
    '''Функция для загрузки справочника в список из файла'''
    try:
        with open("data.csv", "r", newline="") as book_list:
            return list(csv.reader(book_list))
    except FileNotFoundError:
        return []

def save_book(save_list):
    '''Функция для сохранения списка в файл справочника'''
    with open("data.csv", "w", newline="") as book_list:
        file_writer = csv.writer(book_list)
        file_writer.writerows(save_list)




def display_book(page, display_list=None, search_param=None):
    '''Функция для отображения записей постранично либо полным списком
    display_list - параметр для отображения записей при поиске
    search_param - Введенный текст при поиске записи
    '''
    number_entries = 10 # Кол-во записей на одной странице
    fields = ['Фамилия', 'Имя', 'Отчество', 'Организация', 'Рабочий телефон', 'Личный телефон'] # Поля для таблицы справочника
    result_table = PrettyTable(fields) # Таблица для отображаемых записей
    columns = len(fields) # Кол-во столбцов

    if display_list:
        all_row = len(display_list)
        file_reader = display_list
    else:
        file_reader = file_book
        all_row = len(file_reader)

    if page == 0:
        if search_param:
            print(f'Все записи с текстом "{search_param}"')
        else:
            print(f'Все записи')
        for row in file_reader:
            result_table.add_row(row[:columns])
    elif page <= all_row//number_entries:
        print(f'Страница {page}')
        for row in file_reader[number_entries*(page-1):number_entries*page]:
            result_table.add_row(row[:columns])
    elif page == all_row//number_entries + 1:
        print(f'Страница {page}')
        for row in file_reader[number_entries*(page-1):]:
            result_table.add_row(row[:columns])
    elif page > all_row//number_entries + 1:
        print(f'Такой страницы не существует, выберите страницу меньше {page}')

    print(result_table)

def add_book():
    '''Функция для добавления новой записи в справочник'''
    file = file_book # Файл для сохраения новой записи
    list_fields = input('Введите Фамилию, Имя, Отчество, Организацию, Рабочий телефон, Личный телефон через запятую:').split(',') # Список значений полей для новой записи
    file.append(list_fields)
    save_book(file)
    print('Запись успешно добавлена')

def search_and_edit(action):
    '''Функция для поиска записи по вводимому тексту и для редактирования по необходимости
    action - паараметр для выбора действия (поиск или редактирование)
    '''
    file_list = file_book # Загруженный полный список записей
    search_text = input('Введите текст для поиска по справочнику:').lower() # Текст для поиска
    result_list = [row for row in file_list if any(search_text in field.lower() for field in row)] # Список записей исходя из поиска
    if action == 'edit':
        display_book(0, result_list, search_text)
        if len(result_list) > 1:
            print('Найдено больше одной записи, скорректируйте поиск для редактирования')
            search_and_edit('edit')
        elif len(result_list) == 1:
            field_dic = {}
            print('0. Фамилия')
            print('1. Имя')
            print('2. Отчество')
            print('3. Организация')
            print('4. Рабочий телефон')
            print('5. Личный телефон')
            field_list = input('Выберите поля для редактирования через запятую:').split(',')
            for item in field_list:
                field_dic[item] = input(f'Введите новое значение для пункта {item}:')
            for row in file_list:
                if any(search_text in field.lower() for field in row):
                    for point, field_value in field_dic.items():
                        file_list[file_list.index(row)][int(point)] = field_value
            save_book(file_list)
            print('Запись в справочнике успешно изменена')
    elif action == 'search':
        display_book(0, result_list, search_text)


if __name__ == "__main__":
    file_book = load_book()

    while True:
        print("Меню телефонного справочника:")
        print("1. Показать записи")
        print("2. Добавить новую запись")
        print("3. Поиск или редактирование записи")
        print("4. Выход")
        choice = input("Введите выбранный пункт: ")

        match choice:
            case "1":
                page_num = int(input("Введите номер страницы, при значении 0 вывод всех записей целиком: "))
                display_book(page_num)
            case "2":
                add_book()
            case "3":
                print("Выберите действие:")
                print("1. Поиск записи")
                print("2. Редактирование записи")
                choice_point = input("Введите выбранный пункт: ")
                if choice_point == '1':
                    choice_search_or_edit = 'search'
                elif choice_point == '2':
                    choice_search_or_edit = 'edit'
                search_and_edit(choice_search_or_edit)
            case "4":
                print("До свидания!")
                break
        if int(choice) > 4:
            print("Неверный выбор. Пожалуйста, выберите еще раз.")
