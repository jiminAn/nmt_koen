from konlpy.tag import Mecab
import sys
input_file = sys.argv[1]
tokenizer = Mecab()

with open(input_file, 'r') as f:
    for line in f.readlines():
        tokenized_line = tokenizer.morphs(line)
        print(' '.join(tokenized_line).strip())