#!/bin/bash

DATE=`date +%Y-%m-%d`

if [ $# -eq 0 ]
    then echo "Filename, please"
    exit 0
fi

mv $1 $DATE.txt
