#Вариант 13.Создайте базовый класс "Человек" со своиствами
#"имя","возраст" и "пол". От этого класса унаследуйте классы
#"Мужчина" и "Женщина" и добавьте в них свойства,связанные
#с социальным положением
class Human:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
class Man(Human):
    def __init__(self,name,age,sex,married,kids,work):
        Human.__init__(self,name,age,sex)
        self.married=married
        self.kids=kids
        self.work=work
class Woman(Human):
    def __init__(self,name,age,sex,married,kids,work):
        Human.__init__(self,name,age,sex)
        self.married=married
        self.kids=kids
        self.work=work
katya=Human('Катя',22,'жен')
ivan=Man('Иван',34,'муж',True,2,'продавец')
print(katya.__dict__)
print(ivan.__dict__)