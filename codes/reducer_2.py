#!/usr/bin/env python
import sys
from collections import Counter

current_doc = None
word_counter = Counter()

for line in sys.stdin:
    doc_word, count = line.strip().split("\t", 1)
    doc_id, word = doc_word.split(",", 1)
    count = int(count)

    if current_doc == doc_id:
        word_counter[word] += count
    else:
        if current_doc:
            for word, count in word_counter.most_common(3):  # Top 3 words
                print(f'{current_doc},{word}\t{count}')
        current_doc = doc_id
        word_counter = Counter({word: count})

if current_doc == doc_id:
    for word, count in word_counter.most_common(3):  # Top 3 words
        print(f'{current_doc},{word}\t{count}')
