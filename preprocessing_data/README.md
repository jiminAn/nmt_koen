# Data preprocessing for NMT

# 1. clean the data
- remove special symbols
- remove sentence length < 5 or length > 70
```
python cleaning.py koen > koen.clean
```

# 2. Truecasing
- convert lower case in alphabet
```
python truecasing.py koen.clean > koen.clean.true
```

# 3. split the data
```
cut -f1 koen.clean.true > koen.clean.true.ko
cut -f2 koen.clean.true > koen.clean.true.en

```

# 4. Tokenizing
- with mecab
```
python ko_tokenizer.py koen.clean.true.ko > koen.clean.true.ko.tok
python en_tokenizer.py koen.clean.true.en > koen.clean.true.en.tok
```

## 5. Byte Pair Encoding
ref [subword-nmt](https://github.com/rsennrich/subword-nmt)
