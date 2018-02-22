from pycrfsuite import Tagger
from pycrfsuite import ItemSequence
import pprint
import json

from process_data.featuresFactory import SentenceFeaturesFactory
from process_data.sentence import Sentence

pp = pprint.PrettyPrinter(indent=2)

algorithms = ['lbfgs',  # 0 for Gradient descent using the L-BFGS method,
              'l2sgd',  # 1 for Stochastic Gradient Descent with L2 regularization term
              'ap',     # 2 for Averaged Perceptron
              'pa',     # 3 for Passive Aggressive
              'arow'    # 4 for Adaptive Regularization Of Weight Vector
              ]
alg = algorithms[4]
tagger = Tagger()
tagger.open('../var/models/word_feature_'+alg+'.model')


def tag_sent(sent_str):
    list_of_lines = [(id_line + 1, token, 'X', 'X')
                     for id_line, token in enumerate(sent_str.split(' '))]
    sentence = Sentence('test', list_of_lines)
    for i, token in enumerate(sentence.tokens):
        sentence_factory = SentenceFeaturesFactory(sentence, i, training=False)
        features_list = sentence_factory.features
        features = ItemSequence(features_list)
        sentence.outer_labels_pred[:i] = tagger.tag(features)
    sentence.outer_labels_pred.append('O')
    return sentence


sent_str = "Seit 2015 arbeitet Alina bei Tezenis ."
sentence = tag_sent(sent_str)
result = list(zip(sentence.tokens, sentence.outer_labels_pred))
print(sentence.outer_labels_pred)
result = [{"token": token,
           "label": sentence.outer_labels_pred[i]}
          for i, token in enumerate(sentence.tokens)]
pp.pprint(result)

result_json = json.dumps(result)
print(result_json)
