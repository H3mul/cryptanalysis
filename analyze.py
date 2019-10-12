import sys
import re
import argparse


###########################
# Import breakers

from lantern.analysis import frequency
from lantern.fitness import ngram

from break_caesar import break_caesar
from break_caesarbox import break_caesarbox
from break_atbash import break_atbash

###########################
# Helper Funcs

def printDecryptions(decryptions):
    print()
    for decryption in decryptions[:5]:
        print("{:<s} (score:{:<.5f}) key:{:<s} ".format(*decryption))
    print()


###########################
# Arg parsing


parser = argparse.ArgumentParser(description='Analyze ciphertext for simple ciphers and languages stats.')

ctext_stdin = ""
if not sys.stdin.isatty():
    ctext_stdin = sys.stdin.readlines()
else:
    parser.add_argument('ctext')

args = parser.parse_args()
ctext = ''.join(ctext_stdin).strip() if ctext_stdin else args.ctext

scorer = ngram.NgramScorer(frequency.english.trigrams)


###########################
# Run

print("[+] Analysing ciphertext: | %s |" % ctext)

ioc = frequency.index_of_coincidence(re.sub('[^A-Z]','',ctext.upper()))
ioc_language_map = {'English' : 0.06506, 'French' : 0.07862, 'German' : 0.07180, 'Italian' : 0.07413, 'Portugese' : 0.07786, 'Spanish' : 0.07430, 'Swedish' : 0.05897}
ioc_thres = 0.10 #%
languages = list(filter(lambda x : ioc*(1+ioc_thres) > x[1] and ioc*(1-ioc_thres) < x[1], ioc_language_map.items()))
languages_str = map(lambda x : str(x[0]) + " (" + str(x[1]) + ")", languages)

print("[+] Index of Coincidence: %.5f" % ioc)

if languages:
    print("[+] Candidate languages: %s" % ', '.join(languages_str))
else:
    print("[+] Language IoC:")
    print()
    print(', '.join(map(lambda x: "%s (%.5f)" % (x[0], x[1]), ioc_language_map.items())))
    print()
    
print("[+] Attempting Caesar:")
printDecryptions(break_caesar(ctext, scorer))

print("[+] Attempting Caesar Box:")
printDecryptions(break_caesarbox(ctext, scorer))

print("[+] Attempting Atbash:")
printDecryptions(break_atbash(ctext, scorer))