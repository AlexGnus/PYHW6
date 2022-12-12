#Задайте список из нескольких чисел.
#  Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint
n = int(input('Ввудите количество элементов списка: '))
int_lst = []
[int_lst.append(randint(0,30)) for i in range(0,n)]
#for i in range(0, n):
   # i = random.randint(0, 30)
    #int_lst.append(int(i)) 
print(int_lst)
sum = 0
for i in range(1, len(int_lst), 2):
    sum += int_lst[i]
print(sum)   