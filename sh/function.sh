#!/bin/bash

PRE_IFS=$IFS
IFS="
"

cd /home/dooo
filename="bin_name.txt"    
touch $filename

for i in `ls -al /bin` 
    do
        file=`echo $i | awk '{print $5}'`  
        name=`echo $i | awk '{print $9}'`      
       
       if [ "$name" == "." ] || [ "$name" == ".." ] || [ "$name" == "" ]
            then continue
       fi
             
       echo "$file $name" >> $filename   
    done
IFS=$PRE_IFS

