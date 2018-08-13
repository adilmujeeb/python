# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 19:55:52 2018

@author: adil
"""

import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes or N if no:" % get_close_matches(w, data.keys())[0])
        if yn.lower() == "y":
            return data[get_close_matches(w, data.keys())[0]]
        else:
           return ("Word not found") 
    else:
        return ("Word not found")

word = input("Enter word:")

out = translate(word)

if type(out)==list:
    for i in out:
        print(i)
else:
    print(out)
