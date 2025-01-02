#!/usr/bin/env python
import sys

current_word = None
current_docs = set()

for line in sys.stdin:
    word, doc_id = line.strip().split("\t", 1)
    doc_id = doc_id.strip()  # This removes the newline character from doc_id
    if current_word == word:
        current_docs.add(doc_id)
    else:
        if current_word:
            print(f'{current_word}\t{set(current_docs)}')
        current_word = word
        current_docs = {doc_id}

if current_word == word:
    print(f'{current_word}\t{set(current_docs)}')
