from sys import argv
script_name, product, rate, bonus = argv

def pay_func(product, rate, bonus):
      try:
          paycheck = int(product) * int(rate) + int(bonus)
          return paycheck
      except:
          ValueError

print(f"Выработка: {product} часов.")
print(f"Ставка: {rate} руб.")
print(f"Премия: {bonus} руб.")
print(f"Заработная плата: {pay_func(product, rate, bonus)} руб.")