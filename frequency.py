import sys
import argparse
from lantern.analysis import frequency

parser = argparse.ArgumentParser()
parser.add_argument("ctext")
parser.add_argument("-n", type=int)
parser.add_argument("-m", type=int)
args = parser.parse_args()

counts = frequency.frequency_analyze(args.ctext, args.n)
counts = sorted(counts.items(), key = lambda x : x[1])

m = args.m if args.m else 10
print(counts[:m])
