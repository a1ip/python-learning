#!/usr/bin/env python3

# Файл devtools_test.py
from devtools import rangetest
print(__debug__)          # False, если “python –O main.py”

@rangetest((1, 0, 120))   # persinfo = rangetest(...)(persinfo)
def persinfo(name, age):  # Значение age должно быть в диапазоне 0..120
  print('%s is %s years old' % (name, age))

##@rangetest([0, 1, 12], [1, 1, 31], [2, 0, 2009])
##def birthday(M, D, Y):
##  print('birthday = {0}/{1}/{2}'.format(M, D, Y))

##class Person:
##  def __init__(self, name, job, pay):
##    self.job = job
##    self.pay = pay
##  @rangetest([1, 0.0, 1.0]) # giveRaise = rangetest(...)(giveRaise)
##  def giveRaise(self, percent): # Аргумент 0 – ссылка self на экземпляр
##    self.pay = int(self.pay * (1 + percent))

# Закомментированные строки возбуждают исключение TypeError, если сценарий
# не был запущен командой “python -O”

#persinfo('Bob Smith', 45) # В действительности вызывает onCall(...)
persinfo('Bob Smith', 200) # или person, если был использован аргумент –O
                            # командной строки
##birthday(5, 31, 1963)
#birthday(5, 32, 1963)

##sue = Person('Sue Jones', 'dev', 100000)
##sue.giveRaise(.10)          # В действительности вызывает onCall(self, .10)
##print(sue.pay)              # или giveRaise(self, .10), если использован –O
#sue.giveRaise(1.10)
#print(sue.pay)
