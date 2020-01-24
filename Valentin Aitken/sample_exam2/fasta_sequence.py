from sequence import Sequence


class FastaSequence(Sequence):

    def __init__(self, name, content):
        super(FastaSequence, self).__init__(name, content)

    def parse(self):
        result = {}
        for line in self.content:
            current = line.strip()
            if not current:
                continue
            elif current[0] == '>':
                current_key = current[1:]
            else:
                if current_key in result:
                    result[current_key] = result[current_key] + current
                else:
                    result[current_key] = current
        return result
