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
    sent_words = sentence.tokens
    sent_features = SentenceFeaturesFactory(sent_words)
    features_list.append(sent_features.features)
    labels.append(sentence.outer_labels)

pp.pprint(labels[:2])
pp.pprint(features_list[:2])

algorithms = ['lbfgs',  # 0 for Gradient descent using the L-BFGS method,
              'l2sgd',  # 1 for Stochastic Gradient Descent with L2 regularization term
              'ap',     # 2 for Averaged Perceptron
              'pa',     # 3 for Passive Aggressive
              'arow'    # 4 for Adaptive Regularization Of Weight Vector BEST
              ]
alg = algorithms[4]
trainer = BaseTrainer(algorithm=alg)
trainer.set('max_iterations', 20)
print(trainer.get_params())

for xseq, yseq in zip(features_list, labels):
    features = ItemSequence(xseq)
    trainer.append(features, yseq)
trainer.train('models/word_feature_'+alg+'.model')


print()



print('Done')