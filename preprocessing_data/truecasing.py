import re
import sys

input_file = sys.argv[1]
with open(input_file, 'r') as f:
    for line in f.readlines():
        ko, en = line.split('\t')   
        ko_l = ko.lower().strip()
        en_l = en.lower().strip()
        
        print(ko_l, en_l, sep='\t')