#!/usr/bin/env python3

def intersect(*args):
 res = []
 for x in args[0]: # Сканировать первую последовательность
  for other in args[1:]: # Во всех остальных аргументах
   if x not in other: break # Общий элемент?
  else: # Нет: прервать цикл
   res.append(x) # Да: добавить элемент в конец
 return res

def union(*args):
 res = []
 for seq in args: # Для всех аргументов
  for x in seq: # Для всех элементов
   if not x in res:
    res.append(x) # Добавить новый элемент в результат
 return res
