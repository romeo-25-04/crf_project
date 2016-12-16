class Sentence:
    def __init__(self, source_str, list_of_lines):
        self.source = source_str
        self.sent = list_of_lines
        self.persons = self.filter_labels(['B-PER', 'I-PER', 'B-ORG', 'I-ORG', 'B-LOC', 'I-LOC'])

    def filter_labels(self, labels):
        clean_sent = []
        for Id, word, label, label2 in self.sent:
            if label in labels:
                clean_sent.append((Id, word, label, label2))
            else:
                clean_sent.append((Id, word, 'O', label2))
        return clean_sent