import sys
import re
from functions import replaceLetters
from lantern.analysis import frequency
from lantern.fitness import ngram

def decode(ctext, shift, start = 0):
    i = start
    plain = ""
    n = len(ctext)

    while len(plain) < n:
        plain += ctext[i]
        i = (i + shift) % n
    return plain

def break_caesarbox (ctext, scorer):
    original_ctext = ctext
    ctext = re.sub('[^A-Z]','',ctext.upper())
    runningScore = -99e9
    shift = 2
    decryptions = []
    while shift < 10:
        candidate = decode(ctext, shift)
        score = scorer(candidate)
        if score > runningScore:
            decryptions.append((replaceLetters(candidate, original_ctext) , score, str(shift)))
            runningScore = score
        shift += 1
    return decryptions


def printDecryptions(decryptions):
    for decryption in decryptions[:5]:
        print("{:<s} (score:{:<.5f}) key:{:<s} ".format(*decryption))

if __name__ == "__main__":
    scorer = ngram.NgramScorer(frequency.english.trigrams)
    ctext = sys.argv[1]
    print("[+] Ciphertext:" + ctext)
    shift = 3
    if len(sys.argv) > 2:
        shift = sys.argv[2]
    printDecryptions(break_caesarbox(ctext, scorer))
