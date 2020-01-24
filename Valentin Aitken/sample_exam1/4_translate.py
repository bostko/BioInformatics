# * Да се прочете секвенция от файл [data/dna_chromosome_1.seq] и
#   да се разменят всички символте “А” → “T”, “T” → “A” . Резултатът да се записва в нов файл с име [dna_chromosome_solve_1.seq] (20т.)

complementary_translator = ''.maketrans('ATGC', 'TACG')

with open('data/dna_chromosome_1.seq', 'r') as input_data:
    for line in input_data:
        seq = line.strip()
        with open('dna_chromosome_solve_1.seq', 'w') as out:
            out.write(seq.translate(complementary_translator))
        break
