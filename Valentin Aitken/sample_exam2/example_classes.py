class _Sequence():
    def __init__(self, name, content):
        self.name = name
        self.content = content
    
    def parse(self):
        pass

class Fasta_Sequence(_Sequence):
    def parse(self):
        pass

class Multi_Fasta_Sequence(_Sequence):
    def parse(self):
        pass

class SequenceParser():

    def parse_sequence(self, name, seq_type, seq_content):
        if seq_type == "FASTA":
            seq = Fasta_Sequence(name, seq_content)
            seq.parse()
            return seq
        