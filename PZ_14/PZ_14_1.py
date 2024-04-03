#Вариант 13.В строках исходного текстового файла (dates1.txt) все даты представить
#в виде подстроки. Поместить в новый текстовый файл все даты февраля в формате
#ДД/ММ/ГГГГ
import re
#reg=re.compile(r"\,|\;)
with open('dates1.txt', 'r') as file:
    text = file.read()
    matches = re.findall(r'(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(19|20\d{2})', text)
    result = [f"{i[0]}.{i[1]}.{i[2]}" for i in matches]
    print(result)
with open('dates2.txt', 'w') as file1:
    result1 = [f"{i[0]}/{i[1]}/{i[2]}\n" for i in matches]

    file1.writelines(result1)