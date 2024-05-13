#Для задачи из блока 1 создать дые функции,safe_def и load_def,которые позволяют
#сохранять информацию из экземпляров класса (3 шт.) в файл и загружать её
#обратно. Использовать модуль pickle для серелизации и десерелизации объектов
#Python в бинарном формате.
import pickle
from PZ_16_1 import comp1,comp2,comp3
info=[comp1.__dict__,comp2.__dict__,comp3.__dict__]
def save_def():
    with open ('Computer.bin','wb') as file:
        pickle.dump(info,file)
def load_def():
    with open ('Computer.bin','rb') as file:
        pickle.load(file)

save_def()
load_def()