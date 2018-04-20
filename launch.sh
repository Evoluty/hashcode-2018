#!/bin/bash


python3 main.py

file="outputs/source_code.tar.gz"
if [ -f ${file} ]; then
    rm ${file}
fi
tar zcf ${file} *.py
