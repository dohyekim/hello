#!/bin/bash

for i in {2..9} 
do
    echo "=============== $i단 ================"    
    for j in {1..10}
      
       do 
            echo "$i * $j = $(( $i * $j ))"
                  
       done 
done

