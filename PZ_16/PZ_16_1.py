#Вариант 13. Создайте класс "Компьютер" с атрибутами "марка",
#"процессор" и "оперативная память". Напишите метод,который
#выводит информацию о компьютере в формате "Марка:марка,
#Процессор:процессор, Оперативная память:память"
import pickle
class Computer:
    def __init__(self,brand,processor,ram):
        self.brand=brand
        self.processor=processor
        self.ram=ram
    def vivod(self):
        return (f'Компьютер: {self.brand}, Процессор: {self.processor}, Оперативная память: {self.ram}')
comp1=Computer('lenovo','intel','8ГБ')
comp2=Computer('apple','intel','10ГБ')
comp3=Computer('hp','proc','6ГБ')

print(comp1.vivod())