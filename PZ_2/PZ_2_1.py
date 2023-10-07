#Вариант 13. Дано двузначное число. Вывести число, полученное при перестановке
#цифр исходного числа
number_=input("Введите двузначное число ")
try:
    int(number_) #проверка на тип данных число
except Exception:
       print("Вы ввели что-то не то")
       exit()
number=int(number_)
des=number//10
ed=number%10
reversed_number=ed*10+des
print("Число, полученное при перестановке " \
       f"цифр исходного числа: {reversed_number}")