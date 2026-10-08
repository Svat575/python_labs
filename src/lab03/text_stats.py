import os
from sys import path, stdin
path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from src.lib.text import *

text = stdin.read()
text_nrm = normalize(text)
tokens = tokenize(text_nrm)
freqs = count_freq(tokens)
top_5 = top_n(freqs, 5)

print(f"Всего слов: {len(tokens)}\nУникальных слов: {len(freqs.keys())}\nТоп-5:")