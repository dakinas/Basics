# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня,
# на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения
# параметров a и b и выводить одно натуральное число — номер дня.
first_dist = int(input("Какой результат составил в первый день, км:"))
last_dist = int(input("Задайте целевое расстояние, км:"))
day = 1
step = 1.1
print(f"Ежедневное увеличение результата: {(step - 1):.2f} км")
while last_dist > first_dist:
    print(f"{day}-й день: {first_dist:.2f} км")
    first_dist *= step
    day += 1
print(f"{day}-й день: {first_dist:.2f} км")
