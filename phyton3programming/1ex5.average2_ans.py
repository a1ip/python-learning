#!/usr/bin/env python3

numbers = []

while True:
  line = input("enter a number or Enter to finish: ")
  if line:
    try:
      number = int(line)
    except ValueError as err:
      print(err)
      continue
    numbers += str(number)
  else:
    break

if len(numbers) == 0:
    print("не введенно ни одного числа")
else:
    min=int(numbers[0])
    len_num = len(numbers)
    c1=0
    sum=0
    max=0
    min=int(numbers[0])  

    print ("Количество введенных чисел",len_num,", их значения: ")
    while c1< len_num:
        sum += int(numbers[c1])

        if int(numbers[c1]) < min:
            min = int(numbers[c1])

        if int(numbers[c1]) > max:
            max = int(numbers[c1])

        print(numbers[c1])
        c1 += 1

    print("count =",len_num,"sum =",sum,"lowest =",min,"highest =",max,"average =",sum/len_num)


"""
Дополните программу вычисления среднего значения программным кодом, который сортировал бы список чисел. 
Эффективность не имеет значения, поэтому используйте самый простой способ сортировки, какой только придет вам на ум. 
Отсортировав список, можно будет найти и медиану, которая будет являться значением элемента в середине, 
если список содержит нечетное число элементов, и средним значением от двух средних элементов, если список содержит 
четное число элементов. Найдите медиану и выведите ее вместе с остальной информацией.
-v-
Сортировка пузырьком
for(int i = 0; i < a.length - 1; i++)
    for(int j = 0; j < a.length - i - 1; j++)
        if(a[j] > a[j + 1])
            swap(a[j], a[j + 1]);
-^-
"""
print("Исходный список:",numbers)
#print("Длина исходного списка", len(numbers))
#Сортировка
i=0
while i<len(numbers):
  j=0
  while j<len(numbers)-i-1:
    #
    if numbers[j]>numbers[j+1]:
      #
      tmp=numbers[j]
      numbers[j]=numbers[j+1]
      numbers[j+1]=tmp
    j+=1
  #
  i+=1
print("Отсортированный список:",numbers)
#print("Длина отсортированного списка", len(numbers))

#Поиск середины списка, вычисление медианы
while len(numbers)>2:
  numbers.remove(numbers[0])
  numbers.remove(numbers[len(numbers)-1])
  #print("Отсортированный список:",numbers)
  #print("Длина отсортированного списка", len(numbers))
print("Остаточный список:",numbers)
if len(numbers) == 1:
  print("Медиана =", numbers)
else:
  print("Медиана =", ((int(numbers[0])+int(numbers[1]))/2))

 