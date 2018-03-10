import os

# migrations = 'Migrations'
# current_dir = os.path.dirname(os.path.abspath(__file__))
#
# folder = os.path.abspath(os.path.dirname('C:\Users\magistr\Documents\netology courses\Python_course-master\homework\2.3-paths\Migrations\'))
# counter = None
# if __name__ == '__main__':
#     for file in folder:
#         if file.endswith('.sql'):
#             counter+=1
#     print(counter)
#     pass

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
            with open(abs_path + '\' + file, 'r') as f:
                for line in f:
                    if string in line:
                        result.append(file)
                        break
        for res in result:
            print(migrations + '\\' + res)
        print('Всего: ', len(result))

if __name__ == '__main__':
    find_file()
    pass