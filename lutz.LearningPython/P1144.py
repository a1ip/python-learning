#!/usr/bin/env python3

class Person:
  @rangetest(percent=(0.0, 1.0)) # Проверка с помощью декоратора
  def giveRaise(self, percent):
    self.pay = int(self.pay * (1 + percent))

##class Person:
##  def giveRaise(self, percent): # Проверка с помощью встроенного прогр. кода
##    if percent < 0.0 or percent > 1.0:
##      raise TypeError('percent invalid')
##    self.pay = int(self.pay * (1 + percent))
