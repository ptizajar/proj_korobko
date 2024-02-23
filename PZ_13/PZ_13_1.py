#Вариант 13.Для каждой строки матрицы с нечётным номером найти среднее
#арифметическое её элементов
import random
try:
    st = int(input('Введите количество строк '))
    col = int(input('Введите количество столбцов '))
except:
    print('Вы ввели что-то не то')
matrix = [ [ random.randint(-100, 100) for j in range(col)] for i in range(st) ]
sred=[ sum(matrix[i])/len(matrix[i]) for i in range(0,st,2)]
print(f'Исходная матрица:{matrix} \n'
      f'Среднее арифметическое элементов строк с нечётным номером:{sred}')