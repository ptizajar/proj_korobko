#Вариант 13. Составить список, в который будут включены только
#согласные буквы и привести их к верхнему регистру.
#Список: ['Оттава', 'Москва', 'Пекин', 'Полоцк','Версаль','Дели','Каир']
from functools import reduce

words = ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир']

def makeSoglBig(words):
    sogl = 'БВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
    spis_of_spis = [[*word] for word in words]
    spis_of_letters = reduce(lambda list_, spis_word: list_ + spis_word, spis_of_spis, [])
    sogl_letters = filter(lambda any_letter: any_letter.upper() in sogl, spis_of_letters)
    big_letters = map(lambda any_sogl:any_sogl.upper(), sogl_letters)
    return list(big_letters)

print(f'Список согласных букв в верхнем регистре:{makeSoglBig(words)}')