# Задача №3
def sorted_files(list_file):
    result_task3 = {}
    for f_name in list_file:
        path = os.path.join(os.getcwd(), 'sorted', f_name)
        new_name = f_name
        with open(path, encoding='utf-8') as f_name:
            counter = 0
            for _ in f_name:
                counter += 1
            result_task3[new_name] = counter
        result_task3 =  dict(sorted(result_task3.items(), key=lambda x:x[1]))
    path1 = os.path.join(os.getcwd(), '', "result.txt")
    with open(path1, 'w', encoding="utf-8") as new_file:
        for key, value in result_task3.items():
            path = os.path.join(os.getcwd(), 'sorted', key)
            new_file.write(key + "\n")
            new_file.write(str(value)+"\n")
            with open(path, encoding="utf-8") as txt:
                new_file.write(txt.read() + '\n')

                
files_list = ['1.txt', '2.txt', '3.txt']
sorted_files(files_list)
