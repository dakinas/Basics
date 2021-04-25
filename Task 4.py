# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.
input_str = input("Введите строку: ")
input_word = []
step = 1
for elem in range(input_str.count(' ') + 1):
    input_word = input_str.split()
    if len(str(input_word)) <= 10:
         print(f"{step} {input_word [elem]}")
         step += 1
    else:
         print(f"{step} {input_word [elem] [0:10]}")
         step += 1