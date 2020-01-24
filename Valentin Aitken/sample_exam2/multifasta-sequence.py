from sequence import Sequence


class MultifastaSequence(Sequence):

    def __init__(self, name, content):
        super(MultifastaSequence, self).__init(name, content)
