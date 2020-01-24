from sequence import Sequence


class FastaSequence(Sequence):

    def __init__(self, name, content):
        super(FastaSequence, self).__init__(name, content)
