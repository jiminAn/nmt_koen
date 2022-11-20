# Nueral Machine Translation(KOEN)
- [ref code](https://github.com/kh-kim/simple-nmt)
- [data preprocessing for nmt](https://github.com/jiminAn/nmt_koen/tree/main/preprocessing_data)

## 0. Settings
- conda environment
```
conda create -n simple_nmt python==3.7
conda activate simple_nmt
```

- install package
```
pip install -r requirements.txt
```

## Train
### Transformer
- ref code
```
python train.py --train <train set> --valid <valid set> --lang koen\
--gpu_id 0 --batch_size 128 --n_epochs 30 --max_length 100 --dropout .2 \
--hidden_size 768 --n_layers 4 --max_grad_norm 1e+8 --iteration_per_update 32 \
--lr 1e-3 --lr_step 0 --use_adam --use_transformer --rl_n_epochs 0 \
--model_fn <save model path>
```
- run code

```
python train.py --train ./data/corpus.shuf.train.tok.bpe --valid ./data/corpus.shuf.valid.tok.bpe --lang koen\
--gpu_id 0 --batch_size 128 --n_epochs 30 --max_length 100 --dropout .2 \
--hidden_size 768 --n_layers 4 --max_grad_norm 1e+8 --iteration_per_update 32 \
--lr 1e-3 --lr_step 0 --use_adam --use_transformer --rl_n_epochs 0 \
--model_fn ./models/koen_model_transformer.pth
```

### seq2seq
```
python train.py --train ./data/corpus.shuf.train.tok.bpe --valid ./data/corpus.shuf.valid.tok.bpe --lang koen \
--gpu_id 0 --batch_size 128 --n_epochs 30 --max_length 100 --dropout .2 \
--word_vec_size 512 --hidden_size 768 --n_layers 4 --max_grad_norm 1e+8 --iteration_per_update 2 \
--lr 1e-3 --lr_step 0 --use_adam --rl_n_epochs 0 \
--model_fn ./models/koen_model_seq2seq.pth
```

## Evaluation
### Transformer
1. translate KO->EN
- ref code
```
python translate.py --model_fn <save model path> --gpu_id 0 --lang koen < <test set(ko)>  > <translation result(en)>
```
- run code
```
python translate.py --model_fn ./models/koen_model.pth --gpu_id 0 --lang koen < ./data/corpus.shuf.test.tok.bpe.ko  > ./results/transformer.en
```

2. get BLEU score
- ref code
```
cat <generation text(en)> | ./multi-bleu.perl <reference text(en)>
```
- run code
```
cat ./results/transformer.en.detok | ./multi-bleu.perl ./data/corpus.shuf.test.tok.bpe.en.detok
```

### seq2seq
1. translate KO->EN
- run code
```
python translate.py --model_fn ./models/koen_model_seq2seq.pth --gpu_id 0 --lang koen < ./data/corpus.shuf.test.tok.bpe.ko  > ./results/seq2seq.en
```

2. get BLEU score
- run code
```
cat ./results/seq2seq.en.detok | ./multi-bleu.perl ./data/corpus.shuf.test.tok.bpe.en.detok
```


## Results
### BLEU score
|model|avg|1-gram|2-gram|3-gram|4-gram|
|:---:|:---:|:---:|:---:|:---:|:---:|
|Transformer|43.37|63.5|48.0|37.9|30.6|
|Seq2Seq|38.86|60.9|43.5|33.1|26.0|

