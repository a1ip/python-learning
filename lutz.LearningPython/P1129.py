#!/usr/bin/env python3

registry = {}
def register(obj): # Декоратор функций и классов
  registry[obj.__name__] = obj # Добавить в реестр
  return obj # Возвращает сам объект obj, а не обертку

@register
def spam(x):
  return(x ** 2) # spam = register(spam)

@register
def ham(x):
  return(x ** 3)

@register
class Eggs: # Eggs = register(Eggs)
  def __init__(self, x):
    self.data = x ** 4
  def __str__(self):
    return str(self.data)

print('Registry:')
for name in registry:
  print(name, '=>', registry[name], type(registry[name]))

print('\nManual calls:')
print(spam(2)) # Вызов объекта вручную
print(ham(2)) # Вызовы не перехватываются декоратором
X = Eggs(2)
print(X)

print('\nRegistry calls:')
for name in registry:
  print(name, '=>', registry[name](3)) # Вызов из реестра
