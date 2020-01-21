# * Да се прочете секвенция от файл [data/sequence_1.seq] и да се запише в обратна последователност в нов файл с име [reverse_sequence_1.seq]

# * Да се прочете секвенцията(Fasta формат) от файл [data/fasta_seq_1.fa] и да се намери честотата на срещане на “Т” в секвенцията(15т.)
# * Да се прочете секвенция от файл [data/dna_chromosome_1.seq] и да се разменят всички символте “А” → “T”, “T” → “A” . Резултатът да се записва в нов файл с име [dna_chromosome_solve_1.seq] (20т.)
# * Да се прочете DNA секвенция от файл [data/dna_chromosome_1.seq] и да се преобразува във RNA като резултатът се запише в нов файл като секвенцията е в обратен ред. (15т.)

def dic_mfasta(filepath):
    with open(filepath, "r") as input_data:
        result = {}
        for line in input_data:
            current = line.strip()
            if current[0] == '>':
                current_key = current[1:]
            else:
                if current_key in result:
                    result[current_key] = result[current_key] + current
                else:
                    result[current_key] = current
        return result
    return None
