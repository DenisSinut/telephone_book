Консольный телефонный справочник. Хранится в файле data.csv

Для работы со справочником нужно запустить main.py

Меню телефонного справочника:

1. Показать записи

2. Добавить новую запись

3. Поиск или редактирование записи

4. Выход

1 - Позволяет вывести в консоль список всех записей в справочнике в виде таблицы целиком либо постранично(страницу выбирает пользователь). При указании страницы значения 0 выводятся все записи. Поля таблицы: ['Фамилия', 'Имя', 'Отчество', 'Организация', 'Рабочий телефон', 'Личный телефон']

2 - Позволяет добавить новую запись в справочник, необходимо ввести с консоли значения для всех необходимых полей. После этого в файл справочника добавляется новая запись

3 - Имеет два режима работы: а. Поиск записей по тексту, вводимому с консоли. Результат - таблица всех записей, где поисковый текст содержится хотя бы в одном из полей. б. Поиск записей по тексту, вводимому с консоли. Если найдена одна запись, то появляется возможность редактирования записи. Можно редактировать сразу несколько полей. Если же найдено больше одной записи, то появляется возможность повторного поиска с более конкретным поисковым текстом

4 - Позволяет завершить работу телефонного справочника.


Для работы справочника нужно установить дополнительный модуль prettytable
