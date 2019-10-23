def substring_simple(longer, smaller):
    matched_indexes = []
    for i in range(len(longer) - len(smaller) + 1):
        if longer[i : i + len(smaller)] == smaller:
            matched_indexes.append(i)
    return matched_indexes

with open("sub_string_compare.txt", "r") as data_input:
    seq1 = data_input.readline().rstrip()
    seq2 = data_input.readline().rstrip()
    print("Matched indexes: ", substring_simple(seq1, seq2))
