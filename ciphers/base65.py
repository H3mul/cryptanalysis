import unittest
import argparse

class Base65:
    base65chars = "0123456789AaBbCcDdEeFfGgHhIiJjKklLMmNnOoPpQqRrSsTtUuVvWwXxYyZz._-"

    def shift(text, shift):
        text = list(text)
        text = map(lambda x : Base65.base65chars[(Base65.base65chars.find(x) + shift) % 65], text)
        return ''.join(text)

    def encodeChar(char, baseChars):
        value = ord(char)
        i = 32
        encoded = list("a"*32)
        base = len(baseChars)

        while value > 0:
            i -= 1
            encoded[i] = baseChars[value % base]
            value = int(value/base)

        return ''.join(encoded[i:])

    def encode(ptext):
        ctext = []
        for char in ptext:
            cchar = Base65.encodeChar(char, Base65.base65chars)
            if len(cchar) == 1 :
                ctext.append("0")
            ctext.append(cchar)
        return ''.join(ctext)

    def decode(ctext):
        ptext = []
        for i in range(0,len(ctext),2):
            ch1 = ctext[i]
            ch2 = ctext[i+1]
            idx1 = Base65.base65chars.find(ch1)
            idx2 = Base65.base65chars.find(ch2)

            if idx1 < 0 or idx2 < 0:
                return False

            val = 0
            val += (idx1*(len(Base65.base65chars)) + idx2)
            ptext.append(chr(val))
        return ''.join(ptext)

class TestBase65(unittest.TestCase):
    def setUp(self):
        self.decoded_text = "test"
        self.encoded_text = "1u1N1U1u"
    def test_encoding(self):
        self.assertEqual(Base65.encode(self.decoded_text), self.encoded_text)

    def test_decoding(self):
        self.assertEqual(Base65.decode(self.encoded_text), self.decoded_text)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action="store_true")
    parser.add_argument('--decode', action="store_true")
    parser.add_argument('--encode', action="store_true")
    parser.add_argument("string")
    args = parser.parse_args()

    if args.test:
        unittest.main()
        exit()

    if args.decode:
        ptext = Base65.decode(args.string)
        if ptext: 
            print("[+] Decoded string:")
            print(ptext)
        else:
            print("[-] Decoding failed.")

    if args.encode:
        print("[+] Encoded string:")
        print(Base65.encode(args.string))
