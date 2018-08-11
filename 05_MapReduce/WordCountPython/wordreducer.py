#!/usr/bin/env python
import sys

thisword = None
wordcount = 0
word = None

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    count = int(count)

    if thisword == word:
        wordcount += count
    else:
        if thisword:
            print '%s\t%d' % (thisword, wordcount)
        wordcount = count
        thisword = word

if thisword == word:
    print '%s\t%d' % (thisword, wordcount)
