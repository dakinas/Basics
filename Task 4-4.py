# Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
# соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
# обязательно использовать генератор.
from random import randint

gen_list = [randint(0,20) for i in range (0,30)]
my_list = [el for el in gen_list if gen_list.count(el) == 1]
print(f"Сгенерированный список: {gen_list}")
print(f"Итоговый список: {my_list}")
