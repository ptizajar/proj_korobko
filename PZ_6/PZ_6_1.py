#Вариант 13. Дан список А размера N. Вывести вначае его элементы с чётными номерами
#(в порядке возрастания номеров), а заем - элементы с нечётными номерами (также в
#порядке возрастания номеров): А2,А4,А6,...,А1,А3,А5,....Усовный оператор не использовать
from random import randint
try:
    n = int(input("Введите размер списка "))
except Exception:
    print("Вы ввели что-то не то")
mylist = []
for i in range(1,n+1):
    mylist.append(randint(1,100))
print(f"Исходный список {mylist}")
print("Элементы с нечётными номерами: ")
for i in range(0, n, 2):
    print(mylist[i])
print("Элементы с чётными номерами: ")
for i in range(1, n, 2):
    print(mylist[i])



