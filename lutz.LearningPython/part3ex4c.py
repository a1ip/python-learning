#!/usr/bin/env python3

L = [0, 1, 2, 4, 8, 16, 32, 64]
X = 5

i = 0

if (2 ** X) in L:
  print((2**X), 'at index', L.index(2**X))
else:
  print(X, 'not found')

