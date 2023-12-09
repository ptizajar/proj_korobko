#Вариант 13. Дана строка-предложение на русском языке.Вывести
#самое длинное слово в предложении. Если таких слов несколько, то
#вывести первое из них. Словом считать набор символов, не содержащий
#пробелов, знаков препинания и ограниченный пробелами, знаками
#препинания, знаками препинания или началом\концом строки.
try:
    sentence=input("Введите предложение: ")
    words=sentence.split()
    longest_word=''
    end_word=[]
    for i in words:
        if len(i) > len(longest_word):
            longest_word = i
    for i in longest_word:
        if i.isalpha():
            end_word.append(i)
    word_to_print=''.join(end_word)

    print(f"Самое длинное слово: {word_to_print}")
except Exception:
    print("Вы ввели что-то не то")