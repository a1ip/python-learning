#!/usr/bin/env python3

L = [0, 1, 2, 4, 8, 16, 32, 64]
X = 5

i = 0

while i < len(L):
  if 2 ** X == L[i]:
    print('at index', i)
    break
  i = i+1
else:
  print(X, 'not found')

