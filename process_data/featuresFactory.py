class SentenceFeaturesFactory:
    def __init__(self, sent):
        self.sent = sent
        self.features = self.word_features()

    def word_features(self):
        word_feat = []
        for i, word in enumerate(self.sent):
            if i == 0:
                prevWord = "<BOS>"
            else:
                prevWord = self.sent[i-1]

            if i < len(self.sent) - 1:
                next_word = self.sent[i + 1]
            else:
                next_word = '<EOS>'

            word_dict = {
                'word-1': prevWord,
                'word-1:isCapitalized': prevWord[0].isupper(),
                'word-1:suff4': prevWord[-4:],
                'word-1:isPunct': prevWord in ',.!?',
                'word': word,
                'isCapitalized': word[0].isupper(),
                'suff4': word[-4:],
                'isPunct': word in ',.!?',
                'word+1': next_word,
                'word+1:isCapitalized': next_word[0].isupper(),
                'word+1:suff4': next_word[-4:],
                'word+1:isPunct': next_word in ',.!?'
            }
            word_feat.append(word_dict)
        return word_feat
