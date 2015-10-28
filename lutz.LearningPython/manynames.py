#!/usr/bin/env python3

# manynames.py

X = 11 			# атрибут модуля (11)
						# Глобальное (в модуле) имя/атрибут (X, 
						# или manynames.X)

def f():
	print(X) 	# Обращение к глобальному имени X (11)

def g():
	X = 22 		# локальная переменная в функции (22)
						# Локальная (в функции) переменная (X, 
						# скрывает имя X в модуле)
	print(X)

class C:
	X = 33 					# атрибут класса (33)
									# Атрибут класса (C.X)
	def m(self):
		X = 44 				# локальная переменная в методе (44)
									# Локальная переменная в методе (X)
		self.X = 55 	# атрибут экземпляра (55)
									# Атрибут экземпляра (instance.X)

if __name__ == '__main__':
	print(X) # 11: модуль (за пределами файла manynames.X)
	f() # 11: глобальная
	g() # 22: локальная
	print(X) # 11: переменная модуля не изменилась
	
	obj = C() # Создать экземпляр
	print(obj.X) # 33: переменная класса, унаследованная экземпляром
	
	obj.m() # Присоединить атрибут X к экземпляру
	print(obj.X) # 55: экземпляр
	print(C.X) # 33: класс (она же obj.X, если в экземпляре нет X)
	
	#print(C.m.X) # ОШИБКА: видима только в методе
	#print(g.X) # ОШИБКА: видима только в функции