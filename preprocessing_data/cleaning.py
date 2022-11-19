import re
import sys

input_file = sys.argv[1]
with open(input_file, 'r') as f:
    for line in f.readlines():
        ko, en = line.split('\t')
        ko_r = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s\.\,\?\!]", "", ko)
        en_r = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s\.\,\?\!]", "", en)
        if len(ko_r) >= 5 and len(ko_r) <= 70:
            print(ko_r.strip(), en_r.strip(), sep='\t')


