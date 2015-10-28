#!/usr/bin/env python3

def oops():
	#raise IndexError('This is Index Error')
	#raise KeyError('This is Index Error')
	raise IndexError

def func():
	try:
		oops()
	except IndexError:
		print("Test exception")

func()
