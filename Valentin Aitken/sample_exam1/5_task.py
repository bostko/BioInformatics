#!/usr/bin/python3
# * Да се прочете DNA секвенция от файл [data/dna_chromosome_1.seq] и
#   да се преобразува във RNA като резултатът се запише в нов файл като секвенцията е в обратен ред. (15т.)

with open('data/dna_chromosome_1.seq', 'r') as dna1:
    for line in dna1:
        seq = line.strip()
        with open('rna_chromosome_rev_solve_1.seq', 'w') as out:
            out.write(seq.replace('T', 'U')[::-1])
        break
