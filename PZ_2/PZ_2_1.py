#Вариант 13. Дано двузначное число. Вывести число, полученное при перестановке
#цифр исходного числа
number_=input("Введите двузначное число ")
try:
    int(number_) #проверка на тип данных число
except Exception:
       print("Вы ввели что-то не то")
       exit()
number = int(number_)
des = abs(number)//10
ed = abs(number)%10
reversed_number=abs(ed*10)+abs(des)
if number<0:
    abs_reversed_number=reversed_number*(-1)
else:
    abs_reversed_number=reversed_number
print("Число, полученное при перестановке " \
       f"цифр исходного числа: {abs_reversed_number}")