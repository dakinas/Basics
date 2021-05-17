# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки. Необходимо построчно прочитать файл, вычислить прибыль каждой
# компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней
# прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

import json

with open('text_778.json', mode='w', encoding="utf-8") as file_json:
    with open('text_7.txt', mode='r', encoding="utf-8") as file_new:
        profit = {string.split()[0]: int(string.split()[2]) - int(string.split()[3]) for string in file_new}
        result = [profit, {"Общая прибыль": round(sum([int(i) for i in profit.values() if int(i) > 0]) / len([int(i) for i in profit.values() if int(i) > 0]))}]
    json.dump(result, file_json, ensure_ascii=False, indent =4)