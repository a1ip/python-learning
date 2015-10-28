#!/usr/bin/env python3

"""
добавьте в нее программный код, дающий пользователю возможность определить количество выводимых строк (от 1 до 10 включительно),
передавая число в виде аргумента командной строки. Если программа вызывается без аргумента, 
она должна по умолчанию выводить пять строк, как и раньше.
"""

import random

#tuple (кортежи) - относятся к разряду неизменяемых объектов
t_art=('the','a','an')                          #article, артикли
t_noun=('cat', 'dog', 'man', 'woman')           #существительные
t_verb=('sang', 'ran', 'jumped')                #глагол
t_adv=('loudly', 'quietly', 'well', 'badly')    #adverb, наречие
max=5

while True:
    line = input("enter a number of row or Enter to finish: ")
    if line:
        try:
            max = int(line)
        except ValueError as err:
            print(err)
            continue
    else:
        break

print ("max=",max)

if max == 0:
    max=5

i = 0
l=()
while i < max:
    if (random.randint(1,2))==1:
        l=random.choice(t_art)
        l=l+" "+random.choice(t_noun)
        l=l+" "+random.choice(t_verb)
        l=l+" "+random.choice(t_adv)
    else:
        l=random.choice(t_art)
        l=l+" "+random.choice(t_noun)
        l=l+" "+random.choice(t_verb)
    print(l)
    i+=1
