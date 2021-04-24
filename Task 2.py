# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
num_sec = int(input("Введите время в секундах:"))
num_hours = num_sec // 3600
num_sec -= (num_hours * 3600)
num_min = num_sec // 60
num_sec -= (num_min * 60)
if num_hours < 10:
    num_hours = str(f"0{num_hours}")
if num_min < 10:
    num_min = str(f"0{num_min}")
if num_sec < 10:
    num_sec = str(f"0{num_sec}")
print(f"Время в нормальном формате: {num_hours}:{num_min}:{num_sec}")