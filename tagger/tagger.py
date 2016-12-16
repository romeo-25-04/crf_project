from pycrfsuite import Tagger
from pycrfsuite import ItemSequence
from process_data.get_data import GetData
from process_data.featuresFactory import SentenceFeaturesFactory
import pprint
pp = pprint.PrettyPrinter(indent=2)


data = GetData('./test_data/NER-de-test.tsv')
print(len(data.lines), data.lines[:16])
first_sentence = data.sents[0]
print(first_sentence.source)
pp.pprint(first_sentence.sent[:25])

algorithms = ['lbfgs',  # 0 for Gradient descent using the L-BFGS method,
              'l2sgd',  # 1 for Stochastic Gradient Descent with L2 regularization term
              'ap',     # 2 for Averaged Perceptron
              'pa',     # 3 for Passive Aggressive
              'arow'    # 4 for Adaptive Regularization Of Weight Vector
              ]
alg = algorithms[4]
tagger = Tagger()
tagger.open('models/word_feature_'+alg+'.model')

def tag_sent(word_list):
    sentence = SentenceFeaturesFactory(word_list)
    features_list = sentence.features
    features = ItemSequence(features_list)
    labels = tagger.tag(features)
    # pp.pprint(list(zip(sent, labels)))
    return labels

output = []
for sentence in data.sents:
    sent_words = []
    for (Id, word, label, label2) in sentence.persons:
        sent_words.append(word)
    sent_labels = tag_sent(sent_words)
    labels2 = ['O'] * len(sent_words)

    out_sent = zip(sentence.persons, sent_labels, labels2)
    out_sent = ["\t".join(['\t'.join(line[0]), line[1], line[2]]) for line in out_sent]
    out_sent = '\n'.join(out_sent) + '\n'
    output.append(out_sent)

output = "\n".join(output) + '\n'

with open('results/result_'+alg+'.tsv', 'w') as result_file:
    result_file.write(output)

# print(output)


# For Tests
# sent_str = "Seit 2015 arbeitet Jue Wang bei Gini GmbH ."
# sent_str = "Zuletzt war es Wolfram Graf-Rudolf , Chef des Zoos in Aachen ."
# sent_str = "Die ursprüngliche Apfeldiätspeise „ d Spys “ Das ursprüngliche Birchermues ist eine Schweizer Spezialität und wurde um 1900 Albert Wirz Doktor Birchers neue Weltordnung ."
# tag_sent(sent_str)





