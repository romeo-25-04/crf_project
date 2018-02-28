class Word:
    def __init__(self, line):
        '''
        class Word to strukture worsd
        :param line = tup(position:<int>, word:<str>,
                            outer_label:<str>, inner_label:<str>):
        '''
        self.position = line[0]
        self.token = line[1]
        self.outer_label_gold = line[2] if len(line) > 2 else 'O'
        self.inner_label_gold = line[3] if len(line) > 2 else 'O'
        self.outer_label_pred = line[4] if len(line) > 4 else 'O'
        self.inner_label_pred = line[5] if len(line) > 4 else 'O'
        self.part_of_speech = None

    def __str__(self):
        return "{position}\t{word}\t{out_g}\t{in_g}\t{out_p}\t{in_p}".format(
            position=self.position,
            word=self.token,
            out_g=self.outer_label_gold,
            in_g=self.inner_label_gold,
            out_p=self.outer_label_pred,
            in_p=self.inner_label_pred
        )
