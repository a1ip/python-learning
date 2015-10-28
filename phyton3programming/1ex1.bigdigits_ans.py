#!/usr/bin/env python3

import sys

Zero = [" *** ", "*   *", "*   *", "*   *", "*   *", "*   *", " *** "]
One =  [" * ",   "** ",   " * ",   " * ",   " * ",   " * ",   "***"]
Two =  [" *** ", "*   *", "*   *", "   * ", "  *  ", " *   ", "*****"]
Three =[" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
Four = ["   * ", "  ** ", " * * ", "*  * ", "*****", "   * ", "   * "]
Five = ["**** ", "*    ", "*    ", "**** ", "    *", "    *", "**** "]
Six =  [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
Seven =["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight =[" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
Nine = [" *** ", "*   *", "*   *", " ****", "    *", "*   *", " *** "]

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try:
    digits = sys.argv[1]                    #digits - хранятся введенные цифры
    row = 0                                 #строка
    while row < 7:
        line = " "
        column = 0                          #колонка
        while column < len(digits):         #len(digits) - количество введенных цифр
            number = int(digits[column])    #digits[column] - порядковый номер обрабатываемого числа из введенных, number - обрабатываемое число
            digit = Digits[number]          #Digits[number], digit - массив для обрабатываемого числа
            #line += digit[row] + " "       #digit[row] -  из массива для обрабатываемого числа, в зависимости от строки
            dirow = 0
            while dirow < len(digit[row]):
                if str(digit[row][dirow]) is "*":
                    line += str(number) + ""
                else:
                    line += digit[row][dirow] + ""
                dirow += 1
            line += "  "
            column += 1                     #
        print(line)
        row += 1
except IndexError:
    print("usage: bigdigits.py <number>")
except ValueError as err:
    print(err, "in", digits)

