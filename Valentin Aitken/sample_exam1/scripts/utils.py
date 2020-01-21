def calc_freqs(dna_sequence):
    freqs = {}
    for s in dna_sequence:
        if s in freqs:
            freqs[s] += 1
        else:
            freqs[s] = 1
