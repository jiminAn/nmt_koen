# Data preprocessing for NMT

## run script
1. clean, truecasing, split, tokenizing
- input file: `{file_name}` ko, en data split by '\t'
- output file: `{file_name}.en.tok` and `{file_name}.ko.tok`
```
bash create_koen_tok.sh {file_name}
```
2. train and apply bpe for OOV
```
cd subword-nmt
```
- input file : `{train_set}` after 1.
- output file: bpe code `{train_set}.learn_bpe`, and get applying txt `{train_set}.bpe`
```
bash apply_get_bpe.sh {train_set}
```
- input file : `{valid_set}` after 1.
- output file: get applying txt `{file_name}.bpe`
```
bash get_bpe.sh {valid_set}
```
3. Detokenization
- 
```
```


<details>
<summary>Show Details in each files</summary>
<div>

### 1. clean the data
- remove special symbols
- remove sentence length < 5 or length > 70
```
python cleaning.py koen > ./data/koen.clean
```

### 2. Truecasing
- convert lower case in alphabet
```
python truecasing.py ./data/koen.clean > ./data/koen.clean.true
```

### 3. split the data
```
cd ./data/
```
```
cut -f1 koen.clean.true > koen.clean.true.ko
cut -f2 koen.clean.true > koen.clean.true.en

```

### 4. Tokenizing
- with mecab
```
cd ..
```
```
python ko_tokenizer.py ./data/koen.clean.true.ko > ./data/koen.clean.true.ko.tok
python en_tokenizer.py ./data/koen.clean.true.en > ./data/koen.clean.true.en.tok
```

### 5. Byte Pair Encoding
- ref [subword-nmt](https://github.com/rsennrich/subword-nmt)
0. settings
```
git clone https://github.com/rsennrich/subword-nmt
cd subword-nmt
```
1. train bpe by own data set(both ko,en)
```
python learn_bpe.py --input <own_ko_or_en_train_dataset> --output <ko_or_en_bpe>
```
2. apply bpe in own data set(both ko, en)
```
subword-nmt apply-bpe -c <ko_or_en_bpe> < <own_ko_or_en_train_dataset> > <output>
```

### 6. Detoknization
```
sed -r 's/(@@ )|(@@ ?$)//g' {file_name} > {file_name.detok}
```
</div>
</details>
