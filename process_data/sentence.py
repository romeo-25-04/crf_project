import nltk


class Sentence:
    def __init__(self, source_str, list_of_lines):
        self.source = source_str
        self.sent = list_of_lines
        self.line_ids = []
        self.tokens = []
        self.poss = []
        self.outer_labels = []
        self.inner_labels = []
        self.outer_labels_pred = []
        self.inner_labels_pred = []
        self.process()

    def process(self):
        for line_tup in self.sent:
            self.line_ids.append(line_tup[0])
            self.tokens.append(line_tup[1])
            if len(line_tup) > 2:
                self.outer_labels.append(line_tup[2])
                self.inner_labels.append(line_tup[3])
            if len(line_tup) > 4:
                self.outer_labels_pred.append(line_tup[4])
                self.inner_labels_pred.append(line_tup[5])
        self.poss = [pos
                     for token, pos in nltk.pos_tag(self.tokens, lang="deu")]