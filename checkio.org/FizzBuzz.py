#!/usr/bin/env python3

#Your optional code here
#You can import some modules or create additional functions
num = int(input("Введите положительное целое число в диапазоне от 0 до 1000: "))
print ("Если число делится на 3 и 5, будет показано \"Fizz Buzz\";\nЕсли число делится \
	 на 3, будет показано \"Fizz\";\nЕсли число делится на 5, будет показано \"Buzz\";")
print("Иначе,будет показано введенное число.")
print ("Введено число", num)

def checkio(number):
    #Your code here
    #It's main function. Don't remove this function
    #It's using for auto-testing and must return a result for check.

    #replace this for solution
    if number % 3 == 0 and number % 5 == 0:
    	number = "Fizz Buzz"
    elif number % 3 == 0:
    	number = "Fizz"
    elif number % 5 == 0:
    	number = "Buzz"

    return str(number)
#    return 'Fizz'*(not n%3)+' '*(not n%15)+'Buzz'*(not n%5) or str(n)

print (checkio(num))

#Some hints:
#Convert a number in the string with str(n)

"""
Как это используется: Здесь вы можете научиться как писать простейшую функцию и работать с if-else.
Предусловия: 0 < number ≤ 1000 
"""

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
