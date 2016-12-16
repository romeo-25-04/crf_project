class SentenceFeaturesFactory:
    def __init__(self, sent):
        self.sent = sent
        self.features = self.word_features()

    def word_features(self):
        word_feat = []
        for i, word in enumerate(self.sent):
            if i == 0:
                prevWord = "<START>"
            else:
                prevWord = self.sent[i-1]
            word_dict = {
                'word-1': prevWord,
                'word': word,
                'isCapitalized': word[0].isupper(),
                'suff4': word[-4:],
                'isPunct': word in ',.!?'

            }
            word_feat.append(word_dict)
        return word_feat
