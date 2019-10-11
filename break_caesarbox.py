import sys
import re
from lantern.analysis import frequency
from lantern.fitness import ngram

scorer = ngram.NgramScorer(frequency.english.trigrams)
ctext = sys.argv[1]
ctext = re.sub('[^A-Z]','',ctext.upper())
shift = 3
if len(sys.argv) > 2:
    shift = sys.argv[2]

def decode(ctext, shift, start = 0):
    i = start
    plain = ""
    n = len(ctext)

    while len(plain) < n:
        plain += ctext[i]
        i = (i + shift) % n
    return plain


print("[+] Ciphertext:" + ctext)

runningScore = -99e9
shift = 2
while shift < 10:
    candidate = decode(ctext, shift)
    score = scorer(candidate)
    if score > runningScore:
        print("[*] (" + str(shift) + ") : " + candidate + " (" + str(score) + ")")
        runningScore = score
    shift += 1

