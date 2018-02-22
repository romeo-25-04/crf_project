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
                prevWord2 = "<BOS>"
                prevTag2 = "<BOS>"
                prevPOS2 = "<BOS>"
                prevWord = "<BOS>"
                prevTag = "<BOS>"
                prevPOS = "<BOS>"
            elif i == 1:
                prevWord2 = "<BOS>"
                prevTag2 = "<BOS>"
                prevPOS2 = "<BOS>"
                prevWord = self.sentence.tokens[i - 1]
                prevPOS = self.sentence.poss[i - 1]
                prevTag = self.sentence.outer_labels[i - 1] \
                    if self.training \
                    else self.sentence.outer_labels_pred[i - 1]
            else:
                prevWord2 = self.sentence.tokens[i - 2]
                prevTag2 = self.sentence.outer_labels[i - 2] \
                    if self.training \
                    else self.sentence.outer_labels_pred[i - 2]
                prevPOS2 = self.sentence.poss[i - 2]
                prevPOS = self.sentence.poss[i - 1]
                prevWord = self.sentence.tokens[i - 1]
                prevTag = self.sentence.outer_labels[i - 1] \
                    if self.training \
                    else self.sentence.outer_labels_pred[i - 1]

            if i < len(self.sentence.tokens) - 1:
                next_word = self.sentence.tokens[i + 1]
                next_pos = self.sentence.poss[i + 1]
            else:
                next_word = '<EOS>'
                next_pos = '<EOS>'

            word_dict = {
                'prev_tag': prevTag,
                'prev_tag2': prevTag2,
                'prev_pos': prevPOS,
                'prev_pos2': prevPOS2,
                'next_pos': next_pos
            }
            word_dict.update(self.token_features(word, '0'))
            word_dict.update(self.token_features(prevWord2, '-2'))
            word_dict.update(self.token_features(prevWord, '-1'))
            word_dict.update(self.token_features(next_word, '+1'))
            word_feat.append(word_dict)
        return word_feat

    def token_features(self, token, index):
        return {
            'word_' + index: token,
            'word_' + index + '_lower': token.lower(),
            'word_' + index + '_InNames': token in self.GAZET_NAMES,
            'word_' + index + '_isCapitalized': token[0].isupper(),
            'word_' + index + '_suff4': token[-4:],
            'word_' + index + '_isPunct': token in ',.!?',
            'word_' + index + '_wordShape': word_shape(token),
        }


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
