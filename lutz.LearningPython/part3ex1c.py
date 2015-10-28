#!/usr/bin/env python3

S='t s'
L=[]

for x in S:
	print ('ASCII code for symbol', x, '=', ord(x))
	L.append(ord(x))
print ("\nlist for S as ASCII code:", L)

#or list(map(ord, S))
