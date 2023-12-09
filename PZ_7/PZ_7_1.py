#Вариант 13. Дана строка. Подсчитать количество содержащихся в ней цифр
try:
    my_str=input("Введите строку ")
    count=0
    for i in my_str:
        if i.isdigit():
            count+=1
    print(f"Количество цифр в строке: {count}")
except Exception:
    print("Вы ввели что-то не то")