import pprint
from pycrfsuite import ItemSequence
from pycrfsuite import BaseTrainer

from process_data.get_data import GetData
from process_data.featuresFactory import SentenceFeaturesFactory

pp = pprint.PrettyPrinter(indent=2)


data = GetData('./train_data/NER-de-train.tsv')
first_sentence = data.sents[0]
# print(first_sentence.source)
# pp.pprint(first_sentence.sent[:25])

features_list, labels = [], []
for sentence in data.sents:
    sent_words = []
    for (Id, word, label, label2) in sentence.persons:
        sent_words.append(word)
        labels.append(label)
    sent_features = SentenceFeaturesFactory(sent_words)
    features_list.extend(sent_features.features)

pp.pprint(labels[25:30])
pp.pprint(features_list[:25])
features = ItemSequence(features_list)

trainer = BaseTrainer(algorithm='lbfgs')
trainer.set('max_iterations', 50)
print(trainer.get_params())
trainer.append(features, labels)
trainer.train('models/word_feature.model')


print()



print('Done')