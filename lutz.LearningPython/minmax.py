#!/usr/bin/env python3

def minmax(test, *args):
 res = args[0]
 for arg in args[1:]:
  if test(arg, res):
   res = arg
 return res

def lessthan(x, y): return x < y # См. также: lambda
def grtrthan(x, y): return x > y

print(minmax(lessthan, 4, 2, 1, 5, 6, 3)) # Тестирование
print(minmax(grtrthan, 4, 2, 1, 5, 6, 3))
