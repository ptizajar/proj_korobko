#Вариант 13. Проверить есть ли в пследовательности целых N чисел число К
import random
N = 10
posl = [random.randint(1, 20) for i in range(N)]
try:
 K = int(input('Введите целое число К '))
except:
    print('Вы ввели что-то не то')

result = any(map(lambda x: x == K, posl))

if result:
    print(f"Число {K} найдено в последовательности: {posl}")
else:
    print(f"Число {K} не найдено в последовательности: {posl}")