import re

def replaceLetters(ptext, ctext):
    j = 0
    ctext = list(ctext)
    for i in range(len(ctext)):
        char = ctext[i]
        if re.match('[A-Z]', char):
            ctext[i] = ptext[j]
            j += 1
    return ''.join(ctext)
