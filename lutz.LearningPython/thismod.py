#!/usr/bin/env python3

var = 99 						# Глобальная переменная == атрибут модуля

def local():
  var = 0 						# Изменяется локальная переменная

def glob1():
  global var 					# Глобальное объявление (обычное)
  var += 1 						# Изменяется глобальная переменная

"""
def glob2():
  var = 0 						# Изменяется локальная переменная
  import thismod 				# Импорт самого себя
  glob.var += 1 				# Изменяется глобальная переменная
"""

"""
def glob3():
  var = 0 						# Изменяется локальная переменная
  import sys 					# Импорт системной таблицы
  glob = sys.modules['thismod'] # Получить объект модуля
  								# (или использовать __name__)
  glob.var += 1 				# Изменяется глобальная переменная
"""

def test():
  print(var)
  local(); glob1(); glob2(); glob3()
  print(var)

