def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

# print(f"Результат: {my_func(int(input("Введите:")), int(input("Введите первое значение: ")), int(input("Введите первое значение: ")))}")
print(my_func(int(input("Введите первое значение: ")), int(input("Введите второе значение: ")), int(input("Введите третье значение: "))))
