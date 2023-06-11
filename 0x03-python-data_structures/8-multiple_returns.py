#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        if sentence[0] == '':
            x = None
        else:
            x = sentence[0]

    y = len(sentence)
    return (y, x)
