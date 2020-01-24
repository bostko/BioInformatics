import abc


class Sequence(abc.ABC):
    name: str
    content: str

    def __init__(self, name, content):
        print("Sequence %s %s" %(name, content))
        self.name = name
        self.content = content

    @abc.abstractmethod
    def parse(self):
        pass
