
#!/bin/bash

DATE=`date +%Y-%m-%d --date=yesterday`

if [ $# -lt 2 ]
    then echo "Input two filename, please.."
fi

FN="$DATE.log"
cat $1 > $FN
cat $2 >> $FN
