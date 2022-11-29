#!/bin/bash
data=$1

sed -r 's/(@@ )|(@@ ?$)//g' ${data} > ${data}.detok
