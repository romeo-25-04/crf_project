from pycrfsuite import Tagger
from pycrfsuite import ItemSequence
from process_data.featuresFactory import SentenceFeaturesFactory
import pprint
pp = pprint.PrettyPrinter(indent=2)

tagger = Tagger()
tagger.open('word_feature.model')

# sent_str = "Roman Capsamun arbeitet bei Gini GmbH ."

sent_str = "Zuletzt war es Wolfram Graf-Rudolf , Chef des Zoos in Aachen ."

sent = sent_str.split(' ')

sentence = SentenceFeaturesFactory(sent)

features_list = sentence.features
features = ItemSequence(features_list)

labels = tagger.tag(features)
pp.pprint(list(zip(sent, labels)))

