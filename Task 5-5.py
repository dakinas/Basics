# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна
# подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

with open('text_new.txt', mode='w+', encoding="utf-8") as file_new:
    file_new.write(" ".join([str(randint(1, 1000)) for _ in range(20)]))
    file_new.seek(0)
    print(f"Набор чисел: {file_new.readline()}")
    file_new.seek(0)
    print(f"Сумма чисел: {sum(map(int, file_new.readline().split()))}")