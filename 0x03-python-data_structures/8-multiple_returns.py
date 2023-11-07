#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence[0] == "":
        sentence[0] = None
    length = len(sentence)
    first = sentence[0] if sentence is not None else None
    return (length, first)
