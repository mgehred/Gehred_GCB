#!/usr/bin/env python
# coding: utf-8

import sys


def read_fasta(filename):
    """
    Read in a file in FASTA format    
    """
    seq = ''
    f = open(filename)
    for line in f:
        line = line.strip()
        seq = seq + line
    f.close()
    return print(seq)
print(read_fasta(sys.argv[1]))

