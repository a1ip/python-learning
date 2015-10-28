#!/usr/bin/env python3

"""
Создайте списки слов, например, артиклей («the», «a» и других), имен существительных («cat», «dog», «man», «woman»), глаголов («sang», «ran», «jumped») и 
наречий («loudly», «quietly», «well», «badly»).
Затем выполните пять циклов и на каждой итерации 
- с помощью функции random.choice() выберите артикль, существительное, глагол и наречие. 
- с помощью функции random.randint() выберите одну из двух структур предложений: 
артикль, существительное, глагол и наречие - 1
или артикль, существительное и глагол - 2
– и выведите предложение.
Ниже приводится пример запуска такой программы:
awfulpoetry1_ans.py
her man heard politely
his boy sang
another woman hoped
her girl sang slowly
the cat heard loudly
Для решения этого упражнения вам потребуется импортировать модуль random. Списки могут занимать порядка 4–10 строк, в зависимости от того, как много слов вы подберете для каждого из них
и сам цикл будет занимать не более 10 строк, поэтому вся программа, включая пустые строки для лучшей читаемости, должна уместиться примерно в 20 строк.
Решение приводится в файле awfulpoetry1_ans.py.
"""

import random

#tuple (кортежи) - относятся к разряду неизменяемых объектов
t_art=('the','a','an')                          #article, артикли
t_noun=('cat', 'dog', 'man', 'woman')           #существительные
t_verb=('sang', 'ran', 'jumped')                #глагол
t_adv=('loudly', 'quietly', 'well', 'badly')    #adverb, наречие

i = 0
l=()
while i < 5:
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