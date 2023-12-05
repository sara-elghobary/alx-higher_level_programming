#!/usr/bin/python3
def multiple_returns(sentence):
    lenn = len(sentence)
    if lenn == 0:
        return (0, None)
    else:
        return (lenn, sentence[0])
