# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма. Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее
# сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке. Далее запросите
# численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.
earns = int(input("Введите численное значение выручки:"))
costs = int(input("Введите численное значение издержек:"))
if earns >= costs:
    print(f"Вы работаете в прибыль! Ваша рентабельность: {((earns-costs) / earns) * 100}%")
    state = (int(input("Численность персонала:")))
    if state > 0:
        print(f"Прибыль предприятия на одного сотрудника: {((earns - costs) / state)}")
    else:
        state = 1
        print("Количество сотрудников должно быть больше нуля!")
else:
    print("Вы работаете в убыток (")