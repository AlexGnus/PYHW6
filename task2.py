#Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]
from random import randint

number = int(input('Введите количество элементов в списке: '))
lst = []
lst2 = []
[lst.append(randint(0, 10)) for i in range(number)]
#for i in range(number):
   # lst.append(randint(0, 10))

for i in range(len(lst)):
    while i < len(lst)/2 and number > len(lst)/2:
        number = number - 1
        a = lst[i] * lst[number]
        lst2.append(a)
        i+=1

print(lst)
print(lst2)


