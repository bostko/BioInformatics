#!/usr/bin/python3

# * Да се намери честотата на срещане на “А” Аденин в секвенцията: ATAGTGGGAAGATTTATA

from utils import calc_freqs

sequence = 'ATAGTGGGAAGATTTATA'
print("Calculating frequency of a DNA sequence: " + sequence)

print(calc_freqs(sequence)['A'])
