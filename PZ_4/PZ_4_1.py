#Вариант 13. Дано вещественное число А и целое число N(>0).
#Найти A в степени N: A^N=AA...*A (числа А перемножаются N раз).
try:
    a = float(input("Введите число А "))
    n = int(input("Введите положительное число N "))
    number = a**n
    print(f"A в степени N равно {number}")
except Exception:
    print("Вы ввели что-то не то")