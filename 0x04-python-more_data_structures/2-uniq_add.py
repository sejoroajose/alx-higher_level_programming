#!/usr/bin/python
def uniq_add(my_list=[]):
    new_list = set()
    for i in my_list:
        new_list.add(i)

    total = sum(new_list)
    return total
