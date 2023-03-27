import os


def dobavlenie(folder_path, file_name):
    #создание нового файла
    open(os.path.join(folder_path, file_name), 'w').close()


def prosmotr(file_path):
    #просмотр файла
    with open(file_path, 'r') as f:
        print(f.read())


def udalenie(file_path):
    # удаление файла
    os.remove(file_path)

def udalit_duplikati(path):
    # удалениt повторяющихся файлов
    file_hashes = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                file_hash = hash(f.read())
                if file_hash in file_hashes:
                    f.close()
                    os.remove(file_path)
                else:
                    file_hashes[file_hash] = file_path


def scanirovanie(folder_path):
    # сканирование папки
    files = os.listdir(folder_path)

    # Сортируем файлы
    sortirovka = sorted(files)

    return sortirovka


def redaktirovanie(folder_path, file_name):
    # редактирование файла
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, 'w') as f:
        #вывод содержимого, для удобства редактирования
        content = f.read()
        print(content)

        #редактирование файла
        new_content = input(f'Ввдите новое содержимое {file_name}: ')
        f.write(new_content)

def menu():
    print('[1]\t сканирование папки')
    print('[2]\t добавить новый файл')
    print('[3]\t посмотреть содержимое файла')
    print('[4]\t удалить файл')
    print('[5]\t отредактировать файл')
    print('[6]\t удалить повторяющиеся файлы в папке')
    print('[7]\t выйти')

    # Получение выбора от юзера
    key = int(input('Ваш выбор: '))

    if key == 1:
        files = scanirovanie(path)
        print(f'Файлы в папке: {files}')
        menu()
    elif key == 2:
        file_name = input('Введите название нового фйла: ')
        dobavlenie(path, file_name)
        menu()
    elif key == 3:
        file_name = input('Введите название файла для просмотра: ')
        prosmotr(os.path.join(path, file_name))
        menu()
    elif key == 4:
        file_name = input('Введите название файла для удаления: ')
        udalenie(os.path.join(path, file_name))
        menu()
    elif key == 5:
        file_name = input('Введите название файла для редактирования: ')
        redaktirovanie(path, file_name)
        menu()
    elif key == 6:
        udalit_duplikati(path)
        files = scanirovanie(path)
        print(f'Файлы в папке: {files}')
        menu()
    elif key == 7:
        print("программа остановлена")



path = input('Введите путь к папке: ')
menu()

