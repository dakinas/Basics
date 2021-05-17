# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

rus_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open('text_4_new.txt', 'w', encoding="utf-8") as file_new:
    with open('text_4.txt', 'r', encoding="utf-8") as file_old:
        file_new.writelines(string.replace(string.split()[0], rus_dict.get(string.split()[0])) for string in file_old)

# ==================================================================================================
# # pip install googletrans==3.1.0a0
#
# from googletrans import Translator
#
# with open('text_4_google.txt', 'w', encoding="utf-8") as file_new:
#     with open('text_4.txt', 'r', encoding="utf-8") as file_old:
#          text = file_old.read()
#     try:
#         file_new.write(Translator().translate(text, dest="ru").text)
#     except AttributeError:
#         print("Не удалось перевести. Попробуйте еще раз")