from pathlib import Path
import enum
from sequence import *

class SequenceType(enum.Enum):
    FASTA = 1
    MULTI_FASTA = 2
    FASTQ = 3

class SequenceParser:
    def parse(self, seq_type, content, seq_name):
        if seq_type == SequenceType.FASTA:
            print('FASTA')
            seq = FastaSequence(seq_name, content)
        elif seq_type == SequenceType.MULTI_FASTA:
            print('MULTI_FASTA')
            seq = MultiFastaSequence(seq_name, content)
        elif seq_type == SequenceType.FASTQ:
            print('FASTQ')
            seq = FastQSequence(seq_name, content)
        else:
            raise ValueError("No such seq_type %s" % seq_type)
        seq.parse(content)
        seq.print()


def main():
    data = {'data/fasta.fa': SequenceType.FASTA, 'data/multi_fasta.mfa': SequenceType.MULTI_FASTA,
            'data/SRR081241.filt.fastq': SequenceType.FASTQ}
    seq_parser = SequenceParser()
    for filename, type in data.items():
        print("Filename %s Type %s" % (filename, type))
        txt = Path(filename).read_text()
        seq_parser.parse(type, txt, filename)
        print("\n")


if __name__ == "__main__":
    main()
