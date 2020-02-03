import abc


class Sequence(abc.ABC):
    name: str
    content: str

    def __init__(self, name, content):
        self.name = name
        self.content = content

    @abc.abstractmethod
    def parse(self):
        pass

    def iterable_content(self, content) -> [str]:
        if isinstance(content, str):
            iterable_content = content.splitlines()
        else:
            raise TypeError("Accepted type is only str. You passed %s" % type(content))
        return iterable_content

    def print(self):
        print("%s Name %s" % (self.__class__.__name__, self.name))
        print("Content %s" % self.content)


class FastaSequence(Sequence):

    def __init__(self, name, content):
        super(FastaSequence, self).__init__(name, content)

    def parse(self, content):
        key = ''
        seq_segments = []
        for line in self.iterable_content(content):
            current = line.strip()
            if not current:
                continue
            elif current[0] == '>':
                if not key:
                    key = current[1:]
                else:
                    raise ValueError('Fasta format must contain only one greater sign')
            else:
                seq_segments.append(current)
        self.name = key
        self.content = ''.join(seq_segments)


class MultiFastaSequence(Sequence):

    def __init__(self, name, content):
        super(MultiFastaSequence, self).__init__(name, content)
        self.sequences = {}

    def parse(self, content):
        prev_name = ''
        seq_segments = []
        for line in self.iterable_content(content):
            current = line.strip()
            if not current:
                continue
            elif current[0] == '>':
                if prev_name:
                    key = prev_name[0:prev_name.index(' ')]
                    self.sequences[key] = FastaSequence(prev_name, ''.join(seq_segments))
                    seq_segments = []
                prev_name = current[1:]

            else:
                seq_segments.append(current)
        self.content = ''.join(seq_segments)
        if seq_segments:
            key = prev_name[0:prev_name.index(' ')]
            self.sequences[key] = FastaSequence(prev_name, ''.join(seq_segments))

    def print(self):
        for k, v in self.sequences.items():
            print("Key %s" % k)
            v.print()
            print("\n")


class FastQSequence(Sequence):
    def __init__(self, name, content):
        super(FastQSequence, self).__init__(name, content)

    def parse(self, content):
        lines = self.iterable_content(content)
        self.name, self.description = lines[0][1:].split(' ')
        self.description += lines[1][1:]
        self.content = lines[1]
        self.quality = lines[3]
