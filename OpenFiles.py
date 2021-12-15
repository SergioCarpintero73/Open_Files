# Задача №3
import os


#На вход принимаем путь к каталогу. Идем в каталог, получаем список файлов с расширением "TXT".
#Полученные файлы записываем в список
def get_files():
    files_list = []
    for files in os.listdir('.'):
        if files.endswith('.txt'):
            files_list.append(files)
    return files_list


def safeguard(file):
    if 'result.txt' in file:
        file.remove('result.txt')

#Циклом идем по списку файлов. Читаем их.
#Создаем словарь ключом является название файла, значение - количество строк
#Сортируем по значению.
def get_sorted_dict(files):
    merged_dict = {}
    for name in files:
        with open(name, 'r', encoding='utf-8') as file:
            section = file.readlines()
            count = len(section)
            section.insert(0, f'{count}\n')
            merged_dict[name] = section
    merge_sorted = dict(sorted(merged_dict.items(), key=lambda x: x[1]))
    return merge_sorted



def write_result(merged_files):
    with open('result.txt', 'w', encoding='utf-8') as file:
        for string in merged_files.keys():
            file.write(f'{string} \n')
            file.write(' '.join(merged_files.get(string)))
            file.write('\n')


# def sorting_files(list_files):
#     list_names = []
#     for item in list_files:
#         i = 0
#         with open(item, 'r', encoding="utf-8") as file:
#             for line in file:
#                 i += 1
#         list_names.append([item, i])
#
#     list_names.sort(key=lambda z: z[1])
#
#     with open('result.txt', 'w', encoding="utf-8") as file_write:
#         for item in list_names:
#             with open(item[0], 'r', encoding="utf-8") as file_read:
#                 file_write.write(f'{item[0]}\n')
#                 file_write.write(f'{item[1]}\n')
#                 for i in file_read:
#                     file_write.write(i)
#                 file_write.write('\n')

def main():
    file = get_files()
    safeguard(file)
    # sorting_files(file)
    merge = get_sorted_dict(file)
    write_result(merge)


main()

