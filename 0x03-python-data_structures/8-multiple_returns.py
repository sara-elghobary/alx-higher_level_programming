#!/usr/bin/python3
def multiple_returns(sentence):
    lenn = len(sentence)
    if lenn is None:
        return (0, sentence[0])
    else:
        return (lenn, sentence[0])
