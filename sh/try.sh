#!/bin/bash

if [ $# -eq 0 ]; then echo "Input the filename, please"
    exit 0
fi

cat $1
