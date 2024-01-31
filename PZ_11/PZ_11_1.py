#Вариант 13. Средствами языка Python сформировать текстовый файл(.txt)
#содержащий последовательность из целых положительных и отрицательных чисел.
#сформировать новый текстовый файл (.txt) следующего вида,предварительно
#выполнив требуемую обраюотку элементов:
#Исходные данные:
#Количество элементов:
#Индекс первого максимального элемента:
#Произведение элементов средней трети:
numbers='-7 13 8 -4 32 -90 88 -1 43'
my_file1=open('nums1.txt','w',encoding='utf-16')
my_file1.write(numbers)
my_file1.close()

my_file1=open('nums1.txt','r',encoding='utf-16')
read_f=my_file1.read()
read_f=read_f.split()
for i in range(len(read_f)):
    read_f[i]=int(read_f[i])
max_index = read_f.index(max(read_f))
umn=read_f[3]*read_f[4]*read_f[5]

my_file2=open('nums2.txt','w',encoding='utf-16')
my_file2.write(f'Исходные данные:{numbers}')
my_file2.write('\n')
my_file2.write(f'Количество элементов: {len(read_f)}')
my_file2.write('\n')
my_file2.write(f'Индекс первого максимального элемента: {max_index}')
my_file2.write('\n')
my_file2.write(f'Произведение элементов средней трети: {umn}')
my_file2.close()
print("Данные успешно записаны в файл")
