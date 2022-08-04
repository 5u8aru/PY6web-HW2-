from abc import ABC, abstractmethod


class AbstractOutput(ABC):
    @abstractmethod
    def iterator(self):
        pass


class OutputConsole(AbstractOutput):
    def __init__(self, data):
        self.data = data

    def iterator(self, func=None, days=0):
        index, print_block = 1, ''
        for record in self.data.values():
            if func is None or func(record):
                print_block += str(record)
                if index < N:
                    index += 1
                else:
                    yield print_block
                    index, print_block = 1, ''
        yield print_block
