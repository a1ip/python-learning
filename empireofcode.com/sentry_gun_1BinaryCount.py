#!/usr/bin/env python3

def count_units(number):
	num=bin(number)
	count=0
	for i in num:
		if i=='1':
			count += 1
	#print (count)
	return count


if __name__ == '__main__':
  # These "asserts" using only for self-checking and not necessary for auto-testing
  assert count_units(4) == 1
  assert count_units(15) == 4
  assert count_units(1) == 1
  assert count_units(1022) == 9
	#count_units(19)
