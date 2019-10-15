import sys
import re

ctext = sys.argv[1]
ctext = re.sub('\s', '', ctext.strip())

chars = []
for char in ctext:
    if not char in chars:
        chars.append(char)
chars = sorted(chars)

print("[+] Text has %d chars:" % len(chars))
print(''.join(chars))
