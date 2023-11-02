#!/usr/bin/python
def uppercase(str):
    result = ''
    for char in str:
        if 'a' <= char<= 'z':
            upper = chr(ord(char) -32)
            result += upper  
        else:
            result += char
    print(result)
