import pickle

path = 'nltk_german_classifier_data.pickle'


with open(path, 'rb') as f:
    tagger = pickle.load(f)
