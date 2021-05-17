# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open('text_1.txt', 'r', encoding="utf-8") as file_new:
    new_line = file_new.readlines()
    for num, string in enumerate(new_line, 1):
        word_num = len(string.split())
        print(f"{num} строка {string} содержит {word_num} слова\n")