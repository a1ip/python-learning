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


#в цикле while предлагать пользователю ввести число, постепенно накапливая список введенных чисел
#когда пользователь завершит работу с программой (простым нажатием клавиши Enter), выводить
#-числа, введенные пользователем,
#-количество введенных чисел,
#-их сумму,
#-наименьшее и наибольшее число
#-и среднее значение (сумма / количество).
#average1_ans.py
#enter a number or Enter to finish: 5
#enter a number or Enter to finish: 4
#enter a number or Enter to finish: 1
#numbers: [5, 4, 1, 8, 5, 2]
#count = 6 sum = 25 lowest = 1 highest = 8 mean = 4.16666666667
