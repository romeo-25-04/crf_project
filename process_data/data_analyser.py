from process_data.get_data import GetData
import pprint
pp = pprint.PrettyPrinter(indent=2)


data = GetData('../var/train_data/NER-de-train.tsv')

names = []
for sentence in data.sents:
    for (Id, word, label) in sentence.sent:
        if label == 'B-PER':
            names.append(word)

pp.pprint(sorted(set(names)))
