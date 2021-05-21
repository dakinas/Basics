# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.
from random import randint

class Matrix:
    def __init__(self, mtx):
        self.mtx = mtx

    def __str__(self):
        return "\n".join('     '.join([f'{el:5}' for el in line]) for line in self.mtx)

    def __add__(self, other):
            sum_mtx = [[int(self.mtx[line][el]) + int(other.mtx[line][el]) for el in range(len(self.mtx[line]))] for line in range(len(self.mtx))]
            return Matrix(sum_mtx)

rows = int(input("Введите количество строк матрицы: "))
columns = int(input("Введите количество столбцов матрицы: "))
mtx_1 = Matrix([[randint(1, 100) for j in range(rows)] for i in range(columns)])
mtx_2 = Matrix([[randint(1, 100) for j in range(rows)] for i in range(columns)])
new_mtx = mtx_1 + mtx_2

print(f"Матрица 1:\n{mtx_1}\n")
print(f"Матрица 2:\n{mtx_2}\n")
print(f"Сумма матриц:\n{new_mtx}")
