#Напишите программу, удаляющую из файла все слова, содержащие "абв".

with open('абв.txt', 'r', encoding='UTF-8' ) as f:
  str1 = f.read()   
print(str1)

find_txt = 'абв'
lst = [i for i in str1.split() if find_txt not in i]
print(lst)
str2 =' '.join(lst)
with open("абв.txt", "w", encoding='UTF-8' ) as f:
  f.write(str2)
