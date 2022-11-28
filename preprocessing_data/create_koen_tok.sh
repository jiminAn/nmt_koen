#!/bin/bash
data=$1

python cleaning.py ${data} > ${data}.clean
python truecasing.py ${data}.clean > ${data}.clean.true
cut -f1 ${data}.clean.true > ${data}.clean.true.ko
cut -f2 ${data}.clean.true > ${data}.clean.true.en

python ko_tokenizer.py ${data}.clean.true.ko > ${data}.clean.true.ko.tok
python en_tokenizer.py ${data}.clean.true.en > ${data}.clean.true.en.tok
