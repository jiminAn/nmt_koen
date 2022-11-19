import json
import pandas as pd
import sys

input_file = sys.argv[1]

with open(input_file, "r") as json_line:
    json_dict = json.load(json_line)
    
json_list = json_dict["data"]
for i in range(len(json_list)):
    ko = json_list[i]['ko']
    en = json_list[i]['en']
    #print(ko, en, sep='\t')
    print(en, ko, sep='\t')
