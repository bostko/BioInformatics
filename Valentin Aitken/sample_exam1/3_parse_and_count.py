#!/usr/bin/python3

# * Да се прочете секвенцията(Fasta формат) от файл [data/fasta_seq_1.fa] и да се намери честотата на срещане на “Т” в секвенцията(15т.)

from parse_mfasta import dic_mfasta
from utils import calc_freqs

filename = 'data/fasta_seq_1.fa'
sequences = dic_mfasta(filename)
if not len(sequences) == 1:
    print(filename + ' must have 1 sequence')
    exit(1)

print('T is met %d times' % calc_freqs(list(sequences.values())[0])['T'])
