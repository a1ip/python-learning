#!/usr/bin/env python3

import shelve
db = shelve.open('persondb') 	# Открыть хранилище в файле с указанным именем

for key in sorted(db): 				# Обойти и отобразить объекты в базе данных
	print(key, '\t=>', db[key]) # Вывод в требуемом формате

sue = db['Sue Jones'] 				# Извлечь объект по ключу
sue.giveRaise(.10) 						# Изменить объект в памяти вызовом метода
db['Sue Jones'] = sue 				# Присвоить по ключу,
															# чтобы обновить объект в хранилище

db.close() 										# Закрыть после внесения изменений
