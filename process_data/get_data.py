from process_data.sentence import Sentence


class Dataset:
    def __init__(self, path):
        self.path = path
        self.lines = None
        self.get_lines()
        self.sents = None
        self.get_sents()

    def get_lines(self):
        with open(self.path, encoding="utf8") as file_handle:
            self.lines = []
            for line in file_handle:
                items = line.strip().split('\t')
                self.lines.append(tuple(items))

    def get_sents(self):
        sent = []
        self.sents = []
        new_source = ''
        counter_sents = 0
        for line in self.lines:
            if line[0] == '':
                self.sents.append(Sentence(new_source, sent))
                sent = []
                counter_sents += 1
                print('Got {}. Sentence'.format(counter_sents))
            elif line[0] == '#':
                new_source = line[1]
            else:
                sent.append(line)

