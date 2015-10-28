#!/usr/bin/env python3

def countLines(name):
	nfile=open(name)
	count=0
	while nfile.readline():
		count += 1
	nfile.close()
	print("число строк в файле ",name," = ",count)

def countChars(name):
	nfile=open(name)
	nmas=nfile.read()
	ccount=0
	for count in range(len(nmas)):
		if nmas[count] !='\n':
			ccount += 1
	print("число символов в файле ", name, " = ", ccount)

def test(name):
	countLines(name)
	countChars(name)

import sys
if __name__ == "__main__":
	test(sys.argv[0])
