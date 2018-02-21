from pycrfsuite import Tagger
from pycrfsuite import ItemSequence
import pprint
from collections import Counter

from process_data.get_data import GetData
from process_data.featuresFactory import SentenceFeaturesFactory

pp = pprint.PrettyPrinter(indent=2)


data = GetData('../var/test_data/NER-de-dev.tsv')
print(len(data.lines), data.lines[:16])
first_sentence = data.sents[0]
print(first_sentence.source)
# pp.pprint(first_sentence.sent[:25])

algorithms = ['lbfgs',  # 0 for Gradient descent using the L-BFGS method,
              'l2sgd',  # 1 for Stochastic Gradient Descent with L2 regularization term
              'ap',     # 2 for Averaged Perceptron
              'pa',     # 3 for Passive Aggressive
              'arow'    # 4 for Adaptive Regularization Of Weight Vector
              ]
alg = algorithms[4]
tagger = Tagger()
tagger.open('../var/models/word_feature_'+alg+'.model')


def tag_sent(sentence_obj, i):
    sentence_factory = SentenceFeaturesFactory(sentence_obj, i, training=False)
    features_list = sentence_factory.features
    features = ItemSequence(features_list)
    labels = tagger.tag(features)
    return labels

output = []
for sentence in data.sents:
    for i, token in enumerate(sentence.tokens):
        sentence.outer_labels_pred[:i] = tag_sent(sentence, i)
    sentence.inner_labels_pred = ['O'] * len(sentence.tokens)

    out_sent = zip(sentence.line_ids, sentence.tokens,
                   sentence.outer_labels, sentence.inner_labels,
                   sentence.outer_labels_pred, sentence.inner_labels_pred)
    out_sent = ["\t".join(line) for line in out_sent]
    out_sent = '\n'.join(out_sent) + '\n'
    output.append(out_sent)

output = "\n".join(output)

with open('results/result_'+alg+'.tsv', 'w') as result_file:
    result_file.write(output)

pp.pprint(output.split('\n')[:20])

# info = tagger.info()
# transition_features = Counter(info.transitions).most_common(10)
# pp.pprint(transition_features)
