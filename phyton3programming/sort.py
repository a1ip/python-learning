#!/usr/bin/env python3

numbers = [9,6,2,4,5,1]
print(numbers)
#Сортировка
i=0
while i<len(numbers):
  j=0
  print("")
  while j<len(numbers)-i-1:
    print(i,j)
    #
    if numbers[j]>numbers[j+1]:
      #
      tmp=numbers[j]
      numbers[j]=numbers[j+1]
      numbers[j+1]=tmp
    print(numbers)
    j+=1
  #
  i+=1
print(numbers)

