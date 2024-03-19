#!/usr/bin/python3

def multiple_returns(sentence):
    listup = ["firstch", 0]
    if len(sentence) == 0:
        listup[1] = "None"
    else:
        listup[1] = sentence[0]
    listup[0] = len(sentence)
    return(listup)
