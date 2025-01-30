# `all` are all words, from http://www.poslarchive.com/math/scrabble/lists/common-5.html

import pandas as pd
from typing import Set

#pulling in list of words from common-7-letter-words.txt
words = pd.read_csv('common-7-letter-words.txt', header=None)

#creating a set of all words 
targets: Set[str] = set(words[0].tolist())



