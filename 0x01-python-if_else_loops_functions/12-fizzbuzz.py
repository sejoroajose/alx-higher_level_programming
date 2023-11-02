#!/usr/bin/python3
def fizzbuzz():
    rel = 0
    for i in range(100):
        if (i % 3 == 0):
            print('Fizz')
        elif (i % 5 == 0):
            print('Buzz')
        elif ((i % 5) & (i % 3) == 0):
            print('FizzBuzz')
        else:
            print(i)
    return(i)
