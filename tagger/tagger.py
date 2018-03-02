from pycrfsuite import Tagger
from pycrfsuite import ItemSequence
import pprint
from collections import Counter

from process_data.get_data import Dataset
from process_data.featuresFactory import SentenceFeaturesFactory

pp = pprint.PrettyPrinter(indent=2)


data = Dataset('var/test_data/NER-de-dev.tsv')
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
tagger.open('var/models/word_feature_'+alg+'.model')


def tag_sent(sentence_obj, i):
    sentence_factory = SentenceFeaturesFactory(sentence_obj, i, training=False)
    features_list = sentence_factory.features
    features = ItemSequence(features_list)
    labels = tagger.tag(features)
    return labels


output = []
for sentence in data.sents:
    tokens = sentence.get_list_of_tokens()
    for i, word in enumerate(sentence.sent):
        prediction_labels = tag_sent(sentence, i+1)
        word.outer_label_pred = prediction_labels[i]
        word.inner_label_pred = 'O'

    out_sent = [str(word) for word in sentence.sent]
    out_sent = '\n'.join(out_sent) + '\n'
    output.append(out_sent)

output = "\n".join(output)

with open('var/results/result_'+alg+'.tsv', 'w', encoding="utf8") as result_file:
    result_file.write(output)

pp.pprint(output.split('\n')[:20])

# info = tagger.info()
# transition_features = Counter(info.transitions).most_common(10)
# pp.pprint(transition_features)
