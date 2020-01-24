# * Да се прочете секвенция от файл [data/sequence_1.seq] и да се запише в обратна последователност в нов файл с име [reverse_sequence_1.seq]

with open('data/sequence_1.seq', 'r') as input_data:
    for line in input_data:
        seq = line.strip()
        with open('reverse_sequence_1.seq', 'w') as out:
            out.write(seq[::-1])
            out.write("\n")
        break
