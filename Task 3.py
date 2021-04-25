# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится месяц (зима, весна,
# лето, осень). Напишите решения через list и dict.
seasons = ["зима", "весна", "лето", "осень"]
seasons_dict = {1 : "зима", 2 : "весна", 3 : "лето", 4 : "осень"}
month = int(input("Введите номер месяца, где январь 1-й: "))
if month == 1 or month == 12 or month == 2:
    print(seasons_dict.get(1))
    print(seasons[0])
elif month == 3 or month == 4 or month ==5:
    print(seasons_dict.get(2))
    print(seasons[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
    print(seasons[2])
elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
    print(seasons[3])
else:
    print("Такого месяца не существует")