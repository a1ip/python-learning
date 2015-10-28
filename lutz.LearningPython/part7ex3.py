#!/usr/bin/env python3
"""
Обработка ошибок.
Напишите функцию safe(func, *args), которая запускает указанную функцию func, передавая ей произвольное
количество аргументов с использованием синтаксиса *name, перехватывает любые исключения, возникающие
в ходе выполнения этой функции и выводит информацию об исключении с использованием функции exc_info из модуля sys.
Затем с помощью своей функции safe запустите функцию oops из упражнения 1 или 2.
Поместите функцию safe в модуль с именем tools.py и передайте ей функцию oops в интерактивном режиме.
Какие сообщения об ошибках вы получили?
Наконец, расширьте свою функцию safe так, чтобы при возникновении исключения она выводила содержимое стека вызовов
с помощью встроенной функции print_exc, расположенной в стандартном модуле traceback (за дополнительной информацией
обращайтесь к руководству по библиотеке языка Python).
"""

def oops():
	raise IndexError
	#raise MyError

def func():
	try:
		oops()
	except IndexError:
		print("Test exception")

func()
