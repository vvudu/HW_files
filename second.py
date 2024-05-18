import os

# открытие на чтение
def read_file_content(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines

# открытие на запись файлов для слияния
def write_merged_file(files_content, output_file_name):
    with open(output_file_name, 'w', encoding='utf-8') as output_file:
        for file_name, lines in files_content:
            output_file.write(f"{file_name}\n")
            output_file.write(f"{len(lines)}\n")
            output_file.writelines(lines)
            output_file.write('\n')

# слияние
def merge_files(file_names, output_file_name):
    files_content = []
    for file_name in file_names:
        lines = read_file_content(file_name)
        files_content.append((file_name, lines))
    
    files_content.sort(key=lambda x: len(x[1]))

    write_merged_file(files_content, output_file_name)

# Выполнение задания
file_names = ['1.txt', '2.txt', '3.txt']
output_file_name = 'merged.txt'
merge_files(file_names, output_file_name)
