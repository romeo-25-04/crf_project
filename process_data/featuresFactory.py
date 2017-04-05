import re


class SentenceFeaturesFactory:

    GAZET_NAMES = ['Roman', 'Jue']

    def __init__(self, sentence, i, training=True):
        self.sentence = sentence
        self.training = training
        self.features = self.word_features(i)

    def word_features(self, last):
        word_feat = []

        for i, word in enumerate(self.sentence.tokens[:last]):
            if i == 0:
                prevWord = "<BOS>"
                prevTag = "<BOS>"
            else:
                prevWord = self.sentence.tokens[i - 1]
                prevTag = self.sentence.outer_labels[i-1] \
                    if self.training \
                    else self.sentence.outer_labels_pred[i-1]

            if i < len(self.sentence.tokens) - 1:
                next_word = self.sentence.tokens[i + 1]
            else:
                next_word = '<EOS>'

            word_dict = {
                'word-1': prevWord,
                'word-1:isCapitalized': prevWord[0].isupper(),
                'word-1:suff4': prevWord[-4:],
                'word-1:isPunct': prevWord in ',.!?',
                'word': word,
                'word_lower': word.lower(),
                'wordInNames': word in self.GAZET_NAMES,
                'isCapitalized': word[0].isupper(),
                'suff4': word[-4:],
                'isPunct': word in ',.!?',
                'word+1': next_word,
                'word+1:isCapitalized': next_word[0].isupper(),
                'word+1:suff4': next_word[-4:],
                'word+1:isPunct': next_word in ',.!?',
                'wordShape': word_shape(word),
                'prev_tag': prevTag
            }
            word_feat.append(word_dict)
        return word_feat


def word_shape(word):
    """
    Encode words attributes
        Upper cased letter     --> X
        lower cased letter     --> x
        Number                 --> d
        Punctuation            --> to itself
        Length                 --> if len < 5: encode all letter
                                   elif no (numbers or punct) in word: encode 2 first and 2 last letters
                                   else:
    """
    encoded = ''
    for ch in word:
        if ch.isupper():
            encoded += 'X'
        elif ch.islower():
            encoded += 'x'
        elif ch.isdigit():
            encoded += 'd'
        else:
            encoded += ch
    if len(encoded) > 4:
        first = encoded[:2]
        last = encoded[-2:]
        center = encoded[2:-2]
        center = re.sub(r"x+", r"x", center)
        center = re.sub(r"(x\.)+", r"x.", center)
        center = re.sub(r"X+", r"X", center)
        center = re.sub(r"d+", r"d", center)
        encoded = first + center + last

    return encoded
