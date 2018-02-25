# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))
abs_path = os.path.join(current_dir + '\\' + migrations)

def find_file():
    folder = os.listdir(abs_path)
    file_list = []
    for file in folder:
        if file.endswith('.sql'):
            file_list.append(file)

    result = []
    while True:
        print('Введите строку: ')
        string=input()
        if result:
            file_list = result
            result = []
        for file in file_list:
            with open(abs_path + '\\' + file, 'r') as f:
                for line in f:
                    if string in f.read():
                        result.append(file)
                        break
        for res in result:
            print(migrations + '\\' + res)
        print('Всего: ', len(result))

if __name__ == '__main__':
    find_file()


