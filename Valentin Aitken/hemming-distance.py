import itertools

def hemmdistance_equal_length(seq1, seq2):
    if (type(seq1) != str):
        raise AssertionError("Seq1 is not string")
    if (type(seq2) != str):
        raise AssertionError("Seq2 is not string")
    if (len(seq1) != len(seq2)):
        raise RuntimeError("Cannot calculate sequences with different length")
    return hemmdistance_equal_length_impl_zip(seq1, seq2)
    
def hemmdistance_equal_length_impl_simple(seq1, seq2):
    distance = 0
    for i in range(0, len(seq1)):
        if (seq1[i] != seq2[i]):
            distance += 1
    return distance
        
def hemmdistance_equal_length_impl_zip(seq1, seq2):
    distance = 0
    for ch1, ch2 in zip(seq1, seq2):
        if (ch1 != ch2):
            distance += 1
    return distance

with open("hemming-distance.txt", "r") as data_input:
    seq1 = data_input.readline().rstrip()
    seq2 = data_input.readline().rstrip()
    
    print("Distance is ", hemmdistance_equal_length(seq1, seq2))
