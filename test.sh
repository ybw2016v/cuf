#!/bin/bash
cp ./test/* ./
python3 cuf.py -t 2dm test.ini
python3 plot.py
display test.gif
