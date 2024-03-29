#!/bin/bash
gpu_num=$1
TRAIN=$2
VALID=$3
MODEL=$4

python train.py --train ${TRAIN} --valid ${VALID} --lang koen --gpu_id ${gpu_num} --batch_size 128 --n_epochs 30 --max_length 100 --dropout .2 --word_vec_size 512 --hidden_size 768 --n_layers 4 --max_grad_norm 1e+8 --iteration_per_update 2 --lr 1e-3 --lr_step 0 --use_adam --rl_n_epochs 0 --model_fn ${MODEL}
