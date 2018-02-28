import pickle
from process_data.word import Word

path = 'german_pos/nltk_german_classifier_data.pickle'


with open(path, 'rb') as f:
    tagger = pickle.load(f)


class Sentence:
    def __init__(self, source_str, list_of_lines):
        self.source = source_str
        self.sent = [Word(line) for line in list_of_lines]
        self.process()

    def process(self):
        tokens = [word.token for word in self.sent]
        for i, (token, pos) in enumerate(tagger.tag(tokens)):
            word = self.sent[i]
            word.part_of_speech = pos

    def get_list_of_tokens(self):
        return [word.token for word in self.sent]

    def get_list_of_outer_label_gold(self):
        return [word.outer_label_gold for word in self.sent]

    def get_list_of_inner_label_gold(self):
        return [word.inner_label_gold for word in self.sent]

    def get_list_of_outer_label_pred(self):
        return [word.outer_label_pred for word in self.sent]

    def get_list_of_inner_label_pred(self):
        return [word.inner_label_pred for word in self.sent]

    def get_list_of_part_of_speech(self):
        return [word.part_of_speech for word in self.sent]
