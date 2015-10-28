#!/usr/bin/env python3

"""
1. Именованные аргументы. Измените функцию adder из упражнения 2 так, чтобы она принимала и вычисляла сумму/конкатенацию трех аргументов:
def adder(good, bad,ugly). После этого определите значения по умолчанию для каждого из аргументов и поэкспериментируйте с функцией в интерак-
тивной оболочке. Попробуйте передавать ей один, два, три и четыре аргумента. Попробуйте передавать аргументы по именам. Будет ли работать та-
кой вызов: adder(ugly=1, good=2)? Почему?
2. Наконец, обобщите новую версию функции adder так, чтобы принимала и вычисляла сумму/конкатенацию
произвольного числа именованных аргументов. Решение будет напоминать то, что было получено в упражнении 3, с той лишь разницей, что вам при-
дется выполнить обход словаря, а не кортежа. (Подсказка: метод dict.keys() возвращает список, который можно обойти с помощью цикла for
или while, но не забудьте обернуть его вызовом функции list в Python 3.0, чтобы обеспечить возможность обращения к элементам по индексам!)
"""
"""
#1.
def adder(good='ggg', bad='bbb', ugly='uuu'):
#	print(good, bad, ugly)
	return (good+bad+ugly)
"""
#2.
def adder(**args):
#	print(args)
	if len(args) == 1:
		print ("only one argument")
		print(args.keys())
	if len(args) > 1:
#		tmp=Null
		for arg in list(args.keys()):
			print(args.get(arg))
			##print (arg[0])
			#tmp+=args.get(arg)
#		print("tmp=",tmp)
#		return(tmp)

#print(adder())
print(adder(a=1,b=2,c=3))
#print(adder('y'))
#print(adder((1,2,3),(4,5,6)))
#print(adder(1.01,2.02))
