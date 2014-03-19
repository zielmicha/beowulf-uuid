#!/usr/bin/env python2.7
import re
import collections
import random
import math
import os

chain = collections.defaultdict(list)
text = open(os.path.join(os.path.dirname(__file__), 'plain.txt')).read()
words = [ word.replace('.', '').replace(',', '')
          for word in text.split() ]
words = [ word for word in words
          if re.match('^[a-zA-Z]+$', word) ]
starts = []

for word in words:
    if word[0] != word[0].lower():
        starts.append(word.lower())

lowerwords = [ word.lower() for word in words ]

chain[None] = starts
for prev, next in zip(lowerwords, lowerwords[1:]):
    chain[prev].append(next)

def generate(bits):
    words = [None]
    used_bits = 0

    while used_bits < bits:
        choose_from = chain[words[-1]]
        used_bits += math.log(len(choose_from)) / math.log(2.)
        next = random.choice(choose_from)
        words.append(next)

    return '-'.join(words[1:])

if __name__ == '__main__':
    for i in xrange(10):
        print generate(bits=128)
