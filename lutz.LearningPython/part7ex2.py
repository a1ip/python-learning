#!/usr/bin/env python3
"""
Объекты исключений и списки.
Измените функцию oops, которую вы только что написали так, чтобы она возбуждала ваше собственное исключение
с именем MyError. Определите свое исключение в виде класса. Затем расширьте инструкцию try в функции,
которая вызывает функцию oops, так чтобы кроме исключения IndexError она перехватывала бы еще и это исключение
и выводила бы перехваченный экземпляр на экран.
"""
class MyError(Exception):
	pass

def oops():
	raise MyError

def func():
	try:
		oops()
	except IndexError:
		print("Test exception")
	except MyError:
		print("Test MyError")

func()
