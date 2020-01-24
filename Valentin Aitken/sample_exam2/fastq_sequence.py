from sequence import Sequence


class FastqSequence(Sequence):
    def __init__(self, name, content):
        super(FastqSequence, self).__init__(name, content)
