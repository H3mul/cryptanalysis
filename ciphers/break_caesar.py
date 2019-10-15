import re
from pycipher import Caesar
from functions import replaceLetters

def break_caesar(ctext, scorer):
    original_ctext = ctext
    ctext = re.sub('[^A-Z]','',ctext.upper())
    # try all possible keys, return the one with the highest fitness
    scores = []
    for i in range(26):
        ptext = Caesar(i).decipher(ctext)
        scores.append((replaceLetters(ptext, original_ctext), scorer(ptext),str(i)))
    return sorted(scores, key = lambda x : x[1], reverse = True)
