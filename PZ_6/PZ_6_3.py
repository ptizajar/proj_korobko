#Вариант 13.Дан список размера N и целое число К (1<K<N).Осуществить
#сдвиг элементов списка влево на К позиций (при этом Аn перейдёт в Аn-k,
#An-1 B An-k-1, Ak+1 B A1, а исходное значение К первых элементов будет потеряно)
#последние К элементов полученного списка положить равными 0.
import random
try:
    N = int(input("Введите размер списка N "))
    K = int(input("Введите число позиций сдвига K "))
except Exception:
    print("Вы ввели что-то не то")

list2 = []
for i in range(1,N+1):
    list2.append(random.randint(-100,100))
print(f"Исходный список {list2}")

for i in range(0,N-K):
    list2[i] = list2[i+K]
for i in range(N-K,N):
    list2[i] = 0
print(f"Сдвиг списка {list2}")