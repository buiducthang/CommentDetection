#! /bin/bash
#SRCPATH = $1
#desPath = $2
#echo $1
cd $1
python train.py
cd $2
cp $1/spam.model ./
cp $1/vocabs.obj ./
