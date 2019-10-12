from pycipher.atbash import Atbash
from functions import replaceLetters


def break_atbash(ctext, scorer):
    ptext = Atbash().decipher(ctext)
    return [(replaceLetters(ptext, ctext), float(scorer(ptext)), "NA")]
