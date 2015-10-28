#!/usr/bin/env python3

import math

def angles(a, b, c):
    if a+b>c and b+c>a and c+a>b:
      arr=[]
      A=round(math.degrees(math.acos((b*b+c*c-a*a)/(2*b*c))))
      arr.append(A)
      #print(arr)
      B=round(math.degrees(math.acos((c*c+a*a-b*b)/(2*c*a))))
      arr.append(B)
      #print(arr)
      C=180-A-B
      arr.append(C)
      #print(arr)
      #print("A=",A,"B=",B,"C=",C)
      return sorted(arr)
    else:
      return [0, 0, 0]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert angles(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert angles(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert angles(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"

