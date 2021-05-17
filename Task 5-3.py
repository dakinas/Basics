# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
# дохода сотрудников.

with open('text_3.txt', 'r', encoding="utf-8") as file_new:
    new_dict = {string.split()[0]: float(string.split()[1]) for string in file_new}
    print(f"Сотрудники с зарплатой менее 20 000\n{[empl[0] for empl in new_dict.items() if empl[1] < 20000]}")
    print(f"Cредняя величина дохода сотрудников = {round(sum(new_dict.values()) / len(new_dict), 2)}")