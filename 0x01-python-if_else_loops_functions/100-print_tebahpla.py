#!/usr/bin/python3

for i in range(ord('z'), ord('a') - 1, -1):
    char = chr(i)
    case = "Y" if (i - ord('z')) % 2 == 0 else "y"
    print("{}".format(char if i % 2 == 0 else char.upper()), end=case)

print()
