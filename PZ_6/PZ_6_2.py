#Дано число R и список размера N. Найти два соседних элемента списка, сумма
#которых наиболее близка к числу R, и вывести эти элементы в порядке
#возрастания их индексов (определение наиболее близких чисел - то есть
#такой элемент Ак, для которого величина |Ak-R| является минимальной)
from random import randint
try:
    n = int(input("Введите размер списка "))
    r = int(input("Введите число R "))
except Exception:
    print("Вы ввели что-то не то")

list1 = []
for i in range(1,n+1):
    list1.append(randint(-100,100))
print(f"Исходный список {list1}")

element1, element2 = list1[0], list1[1]
summa = element1 + element2

for i in range(1, n - 1):
    result=abs(list1[i] + list1[i + 1]-r)
    if result < summa:
        summa=result
        element1, element2 = list1[i], list1[i + 1]

print(f"Первый элемент {element1}, второй элемент {element2}")