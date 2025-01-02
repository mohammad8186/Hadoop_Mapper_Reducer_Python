#!/usr/bin/env python
import sys

for line in sys.stdin:
    doc_id, text = line.strip().split(",", 1)
    words = text.split()
    for word in words:
        print(f'{doc_id},{word}\t1')
