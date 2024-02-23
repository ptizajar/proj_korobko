#Вариант 13. В матрице найти максимальный положительный элемент,кратный 4
import random
def elements(matrix):
    for row in matrix:
        for elem in row:
            yield elem

try:
    st = int(input('Введите количество строк '))
    col = int(input('Введите количество столбцов '))
    matrix = [[random.randint(-100, 100) for j in range(col)] for i in range(st)]
    elem = max(filter(lambda x: x >0 and x % 4 == 0, elements(matrix)))
    print(f'Исходная матрица: {matrix}\n'
          f'Максимальный положительный элемент, кратный 4: {elem}')
except:
    print('Вы ввели что-то не то или сгенерировалась матрица только '
          'из отрицательных чисел =(')

