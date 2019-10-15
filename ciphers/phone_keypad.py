import sys
import re

ctext = ""
if (len(sys.argv) > 1):
    ctext = sys.argv[1]
else:
    for line in sys.stdin:
        ctext += line

cwords = ctext.split() 

words = []
telephone_map = { 2 : "ABC", 3 : "DEF", 4 : "GHI", 5 : "JKL", 6 : "MNO", 7 : "PQRS", 8 : "TUV", 9 : "WXYZ"}
for cword in cwords:
    letter_map = list(map(lambda x: (len(x[0]), int(x[1])), re.findall("(([0-9])\\2*)", cword)))

    word = ""
    for (c, d) in letter_map:
        word += telephone_map[d][c-1] 

    word = re.sub('\d+', word, cword)
    words.append(word)

print("[+] Decoded string:")
print(" ".join(words))
