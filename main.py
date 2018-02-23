import os
import sys
from trainer.trainer import trainer
sys.path.append(os.path.abspath('./var'))
sys.path.append(os.path.abspath('./german_pos'))
print(sys.path)


# trainer.train('var/models/word_feature_'+'arow'+'.model')
# print('Done')

from tagger.tagger_str import tagger
