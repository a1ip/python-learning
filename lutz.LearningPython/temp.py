#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Все следующие литералы строк содержат символы latin-1.
# Если изменить название кодировки в комментарии выше на ascii или utf-8,
# это приведет к появлению ошибок, так как значения 0xc4 и 0xe8 в строке
# myStr1 не являются допустимыми ни в одной из них.

myStr1 = 'aÄBèC'
myStr2 = 'A\u00c4B\U000000e8C'
myStr3 = 'A' + chr(0xC4) + 'B' + chr(0xE8) + 'C'

import sys
print('Default encoding:', sys.getdefaultencoding())

for aStr in myStr1, myStr2, myStr3:
	print('{0}, strlen={1}, '.format(aStr, len(aStr)), end='')
	
	bytes1 = aStr.encode() 	# В utf-8 по умолчанию:
													# 2 байта на каждый символ не-ASCII
	bytes2 = aStr.encode('latin-1') # По одному байту на символ
	#bytes3 = aStr.encode('ascii') 	# Кодирование в ASCII приведет к ошибке:
																	# за пределами диапазона 0..127
	
	print('byteslen1={0}, byteslen2={1}'.format(len(bytes1), len(bytes2)))
