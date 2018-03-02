from pycrfsuite import Tagger
from pycrfsuite import ItemSequence
import pprint
import json
import nltk

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
if __name__ == "__main__":
    tagger.open('var/models/word_feature_'+alg+'.model')
else:
    tagger.open('./var/models/word_feature_' + alg + '.model')


def tag_sent(sent_str):
    list_of_lines = [(id_line + 1, token, 'X', 'X')
                     for id_line, token in enumerate(nltk.word_tokenize(sent_str))]
    sentence = Sentence('test', list_of_lines)
    for i, word in enumerate(sentence.sent):
        sentence_factory = SentenceFeaturesFactory(sentence, i+1, training=False)
        features_list = sentence_factory.features
        features = ItemSequence(features_list)
        word.outer_label_pred = tagger.tag(features)[i]
    return sentence


if __name__ == "__main__":
    sent_str = "Das ist ein magisches test Satz von Roman Capsamun."
    sentence = tag_sent(sent_str)
    result = list(zip(sentence.get_list_of_tokens(), sentence.get_list_of_outer_label_pred()))
    result = [{"token": word.token,
               "label": word.outer_label_pred}
              for word in sentence.sent]
    pp.pprint(result)

    result_json = json.dumps(result)
    print(result_json)
